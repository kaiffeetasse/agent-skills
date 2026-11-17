#!/usr/bin/env python3
"""Transitous-Abfrage fuer Zug-/OEPNV-Verbindungen (DE/CH/AT) - ohne Key.

Warum ein Skript: api.transitous.org braucht einen User-Agent (sonst 403), `time` muss UTC mit
`Z` sein, `arriveBy` wird nicht umgesetzt, `duration` ist in Sekunden, und Tuer-zu-Tuer-Abfragen
lassen Fernverkehr aus. Dieses Skript kapselt all das.

Beispiele:
  # Tuer-zu-Tuer, zwei Abfahrtszeiten
  python3 transitous_plan.py --from "<Straße Hausnr, PLZ Ort>" \\
      --to "Vitalisstrasse 170, 50827 Koeln" --date 2026-11-12 --times 11:30,13:00

  # Bahnhof->Bahnhof (Gegenprobe bei duenner Trefferliste)
  python3 transitous_plan.py --from "Koeln Hbf" --to "<Zielbahnhof>" \\
      --date 2026-11-12 --times 19:00,19:30,20:00 --station

Ausgabe: pro Abfahrt die Itineraries mit Abfahrt/Ankunft in Ortszeit, Dauer, Umstiegen und Legs.
"""
import argparse
import json
import urllib.parse
import urllib.request
from datetime import datetime
from zoneinfo import ZoneInfo

TZ = ZoneInfo("Europe/Berlin")
UTC = ZoneInfo("UTC")
BASE = "https://api.transitous.org/api/v1"
HDR = {"User-Agent": "Mozilla/5.0", "Accept": "application/json"}


def get(url, timeout=90):
    req = urllib.request.Request(url, headers=HDR)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8", "replace"))


def place(text, station=False):
    """Haltestellen-ID, sonst 'lat,lon'. station=True bevorzugt einen STOP-Treffer."""
    hits = get(f"{BASE}/geocode?text={urllib.parse.quote(text)}")
    if not hits:
        raise SystemExit(f"Ort nicht gefunden: {text}")
    if station:
        for h in hits:
            if h.get("id"):
                return h["id"], h["name"]
    h = hits[0]
    if h.get("id"):
        return h["id"], h["name"]
    return f"{h['lat']},{h['lon']}", h["name"]


def plan(frm, to, when_local, n=6):
    utc = when_local.astimezone(UTC).strftime("%Y-%m-%dT%H:%M:00Z")
    url = (f"{BASE}/plan?fromPlace={urllib.parse.quote(frm)}"
           f"&toPlace={urllib.parse.quote(to)}&time={utc}&numItineraries={n}")
    return get(url)


def hm(iso):
    return datetime.fromisoformat(iso.replace("Z", "+00:00")).astimezone(TZ).strftime("%H:%M")


def show(itins, label):
    print(f"\n#### {label}")
    seen = set()
    for it in itins.get("itineraries", []):
        legs = it["legs"]
        key = (legs[0]["startTime"], legs[-1]["endTime"], len(legs))
        if key in seen:
            continue
        seen.add(key)
        mins = int(it["duration"] // 60)
        rides = [l for l in legs if l.get("mode") != "WALK"]
        print(f"\n-- {hm(legs[0]['startTime'])} -> {hm(legs[-1]['endTime'])}  "
              f"({mins // 60}h{mins % 60:02d}, {max(0, len(rides) - 1)} Umstiege)")
        for l in legs:
            if l.get("mode") == "WALK":
                print(f"   {hm(l['startTime'])} Fussweg {round(l.get('distance', 0) or 0)} m"
                      f" -> {l.get('to', {}).get('name')}")
                continue
            line = l.get("routeShortName") or l.get("mode")
            print(f"   {hm(l['startTime'])} {line:7} {str(l.get('headsign', ''))[:32]:32} "
                  f"{l.get('from', {}).get('name')} -> {hm(l['endTime'])} {l.get('to', {}).get('name')}")
        if len(rides) > 5:
            print("   WARNUNG: >5 Umstiege - Datum evtl. ausserhalb des Feed-Horizonts, "
                  "nicht als Verbindung ausgeben.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--from", dest="frm", required=True)
    ap.add_argument("--to", dest="to", required=True)
    ap.add_argument("--date", required=True, help="YYYY-MM-DD")
    ap.add_argument("--times", required=True, help="Ortszeiten, kommagetrennt: 11:30,13:00")
    ap.add_argument("--station", action="store_true",
                    help="beide Orte als Bahnhof/Haltestelle aufloesen (Bahnhof->Bahnhof)")
    ap.add_argument("--n", type=int, default=6, help="Itineraries pro Abfrage")
    a = ap.parse_args()

    frm, fname = place(a.frm, a.station)
    to, tname = place(a.to, a.station)
    print(f"# {fname}  ->  {tname}")
    for t in a.times.split(","):
        t = t.strip()
        when = datetime.fromisoformat(f"{a.date}T{t}:00").replace(tzinfo=TZ)
        try:
            show(plan(frm, to, when, a.n), f"ab {t} Ortszeit")
        except Exception as exc:  # Netz/Timeout: naechste Zeit weiter probieren
            print(f"\n#### ab {t} Ortszeit - FEHLER: {exc!r}")


if __name__ == "__main__":
    main()
