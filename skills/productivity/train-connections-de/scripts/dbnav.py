#!/usr/bin/env python3
"""
dbnav.py - client for the DB Navigator (de.hafas.android.db) "vendo" HAFAS API.

Reverse engineered from db-navigator-26-20-0.xapk (version 26.20.0, Oct 2026).
Base URL : https://app.services-bahn.de
Auth     : none - only the app User-Agent and an X-Correlation-ID are required.

Endpoints used here
    POST /mob/location/search          station / address search
    POST /mob/angebote/fahrplan        connection search incl. cheapest price
    POST /mob/angebote/recon           priced offer details (Sparpreis/Flexpreis/...)
    POST /mob/angebote/tagesbestpreis  best-price-per-time-slice for one day
    POST /mob/bahnhofstafel/abfahrt    departure board

No third-party dependencies (stdlib only).
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
import uuid
from datetime import datetime, timedelta
from typing import Any, Iterable

BASE = "https://app.services-bahn.de"
USER_AGENT = "DBNavigator/Android/26.20.0"
APP_VERSION = "26.20.0"

CT_LOCATION = "application/x.db.vendo.mob.location.v3+json"
CT_TRIPSEARCH = "application/x.db.vendo.mob.verbindungssuche.v9+json"
CT_BOARD = "application/x.db.vendo.mob.bahnhofstafeln.v2+json"


class DbApiError(RuntimeError):
    def __init__(self, status: int, body: str) -> None:
        self.status = status
        self.body = body
        super().__init__(f"HTTP {status}: {body[:300]}")


def _post(path: str, body: dict[str, Any], content_type: str) -> Any:
    data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(BASE + path, data=data, method="POST")
    req.add_header("Content-Type", content_type)
    req.add_header("Accept", content_type)
    req.add_header("User-Agent", USER_AGENT)
    # Mandatory. Without it the gateway answers 405, without the User-Agent 452 OPS_BLOCKED.
    req.add_header("X-Correlation-ID", str(uuid.uuid4()))
    req.add_header("X-Device-Os-Name", "Android")
    req.add_header("X-Device-Os-Version", "34")
    req.add_header("X-Device-Model", "Google Pixel 7")
    req.add_header("X-App-Version", APP_VERSION)
    req.add_header("Accept-Language", "de-DE, de;q=0.9")
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        raise DbApiError(exc.code, exc.read().decode("utf-8", "replace")) from exc


# --------------------------------------------------------------------------- #
# station search
# --------------------------------------------------------------------------- #
def search_stations(term: str, limit: int = 5) -> list[dict[str, Any]]:
    """POST /mob/location/search -> list of {locationId, evaNr, name, ...}."""
    return _post(
        "/mob/location/search",
        {"searchTerm": term, "maxResults": limit},
        CT_LOCATION,
    )


def resolve_station(term: str) -> dict[str, Any]:
    hits = search_stations(term, limit=1)
    if not hits:
        raise SystemExit(f"no station found for {term!r}")
    return hits[0]


# --------------------------------------------------------------------------- #
# connection search (+ prices)
# --------------------------------------------------------------------------- #
def _traveller(
    typ: str = "ERWACHSENER",
    alter: int | None = None,
    ermaessigungen: Iterable[str] | None = None,
) -> dict[str, Any]:
    t: dict[str, Any] = {"reisendenTyp": typ}
    if alter is not None:
        t["alter"] = alter
    if ermaessigungen is not None:
        t["ermaessigungen"] = list(ermaessigungen)
    return t


def build_travellers(
    pax: int = 1,
    bahncard: str | None = None,
    klasse: str = "KLASSE_2",
    extra: Iterable[str] = (),
    children: Iterable[int] = (),
) -> list[dict[str, Any]]:
    """
    Passenger list for the request.

    Count  : one object per person - the API has no `anzahl` field.
    BahnCard: the key is class-bound and contains a space, e.g. "BAHNCARD25 KLASSE_2"
              (plain "BAHNCARD25" -> 400 MODA/FATAL).
    Children: JUGENDLICHER needs `alter`, otherwise it is priced as an adult.
    """
    erm: list[str] = []
    if bahncard:
        erm.append(f"BAHNCARD{bahncard} {klasse}")
    erm.extend(extra)

    adult: dict[str, Any] = {"reisendenTyp": "ERWACHSENER"}
    if erm:
        adult["ermaessigungen"] = erm
    travellers = [dict(adult) for _ in range(max(pax, 1))]
    travellers.extend({"reisendenTyp": "JUGENDLICHER", "alter": age} for age in children)
    return travellers


def search_connections(
    from_location_id: str,
    to_location_id: str,
    when: datetime,
    *,
    klasse: str = "KLASSE_2",
    travellers: list[dict[str, Any]] | None = None,
    max_changes: int | None = None,
    context: str | None = None,
    fahrrad: bool = False,
) -> dict[str, Any]:
    """
    POST /mob/angebote/fahrplan

    Returns the raw LoesungsmoeglichkeitenModel:
        {"verbindungen": [{"verbindung": {...}, "angebote": {...}}],
         "frueherContext": "...", "spaeterContext": "..."}

    Each entry already contains the cheapest price in
    angebote.preise.gesamt.ab (or .einzel.ab) without a follow-up call.
    """
    wunsch: dict[str, Any] = {
        "abgangsLocationId": from_location_id,
        "zielLocationId": to_location_id,
        "zeitWunsch": {
            "reiseDatum": when.strftime("%Y-%m-%dT%H:%M:%S"),
            "zeitPunktArt": "ABFAHRT",
        },
    }
    if max_changes is not None:
        wunsch["maxUmstiege"] = max_changes
    if fahrrad:
        wunsch["fahrradmitnahme"] = True
    if context:
        wunsch["context"] = context

    return _post(
        "/mob/angebote/fahrplan",
        {
            "reiseHin": {"wunsch": wunsch},
            "reisendenProfil": {"reisende": travellers or [_traveller()]},
            "klasse": klasse,
            "reservierungsKontingenteVorhanden": False,
        },
        CT_TRIPSEARCH,
    )


# --------------------------------------------------------------------------- #
# priced offer details
# --------------------------------------------------------------------------- #
def connection_offers(
    verbindung: dict[str, Any],
    *,
    klasse: str = "KLASSE_2",
    travellers: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    """
    POST /mob/angebote/recon

    Needs the `kontext` blob of one connection from the fahrplan response.
    Returns BepreisteVerbindungModel with angebote.angebotsCluster containing the
    bookable products (Super Sparpreis, Sparpreis, Flexpreis, reservations,
    upsells, ...) including per-offer ids and prices.
    Pass the same traveller/BahnCard list as in the search - otherwise the
    returned prices are undiscounted.
    """
    return _post(
        "/mob/angebote/recon",
        {
            "klasse": klasse,
            "reisendenProfil": {"reisende": travellers or [_traveller()]},
            "reservierungsKontingenteVorhanden": False,
            "verbindungHin": {"kontext": verbindung["kontext"]},
        },
        CT_TRIPSEARCH,
    )


def day_best_prices(
    from_location_id: str,
    to_location_id: str,
    day: datetime,
    *,
    klasse: str = "KLASSE_2",
    travellers: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    """
    POST /mob/angebote/tagesbestpreis

    Returns {"tagesbestPreisIntervalle": [{intervallAb, intervallBis,
             istBestpreis, angebotsPreis, verbindungen: [...]}], "nachrichten": []}
    """
    return _post(
        "/mob/angebote/tagesbestpreis",
        {
            "reiseHin": {
                "wunsch": {
                    "abgangsLocationId": from_location_id,
                    "zielLocationId": to_location_id,
                    "zeitWunsch": {
                        "reiseDatum": day.strftime("%Y-%m-%dT00:00:00"),
                        "zeitPunktArt": "ABFAHRT",
                    },
                }
            },
            "reisendenProfil": {"reisende": travellers or [_traveller()]},
            "klasse": klasse,
        },
        CT_TRIPSEARCH,
    )


def departures(eva_nr: str, day: datetime) -> dict[str, Any]:
    """POST /mob/bahnhofstafel/abfahrt (live departure board)."""
    return _post(
        "/mob/bahnhofstafel/abfahrt",
        {"ursprungsBahnhofId": eva_nr, "datum": day.strftime("%Y-%m-%d"), "verkehrsmittel": []},
        CT_BOARD,
    )


# --------------------------------------------------------------------------- #
# helpers
# --------------------------------------------------------------------------- #
def cheapest_price(offer_block: dict[str, Any]) -> tuple[float | None, float | None]:
    """(price, strikethrough) from an `angebote` block."""
    preise = offer_block.get("preise") or {}
    rahmen = preise.get("gesamt") or preise.get("einzel") or {}
    ab = (rahmen.get("ab") or {}).get("betrag")
    streich = ((rahmen.get("streichpreis") or {}).get("preis") or {}).get("betrag")
    return ab, streich


def _leg_label(leg: dict[str, Any]) -> str:
    kurz = (leg.get("kurztext") or "").strip()
    nummer = (leg.get("verkehrsmittelNummer") or "").strip()
    if kurz and nummer.startswith(kurz):
        return nummer
    return f"{kurz} {nummer}".strip() or "Fußweg"


def connection_rows(payload: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for item in payload.get("verbindungen", []):
        v = item["verbindung"]
        legs = v.get("verbindungsAbschnitte") or []
        if not legs:
            continue
        price, streich = cheapest_price(item.get("angebote") or {})
        rows.append(
            {
                "departure": legs[0].get("abgangsDatum"),
                "arrival": legs[-1].get("ankunftsDatum"),
                "duration_min": round(v.get("reiseDauer", 0) / 60),
                "changes": v.get("umstiegeAnzahl", 0),
                "trains": " + ".join(
                    _leg_label(leg)
                    for leg in legs
                ),
                "from": (legs[0].get("abgangsOrt") or {}).get("name"),
                "to": (legs[-1].get("ankunftsOrt") or {}).get("name"),
                "price": price,
                "strike": streich,
                "messages": "; ".join((item.get("angebote") or {}).get("angebotsMeldungen") or []),
                "kontext": v.get("kontext"),
            }
        )
    return rows


def _fmt_time(iso: str | None) -> str:
    if not iso:
        return "??:??"
    return datetime.fromisoformat(iso).strftime("%H:%M")


def print_rows(rows: list[dict[str, Any]]) -> None:
    print(f"{'dep':>5} {'arr':>5} {'dur':>5} {'um':>2}  {'price':>8}  trains")
    print("-" * 78)
    for r in rows:
        price = "-" if r["price"] is None else f"{r['price']:.2f} EUR"
        if r["strike"]:
            price += f" (statt {r['strike']:.2f})"
        print(
            f"{_fmt_time(r['departure']):>5} {_fmt_time(r['arrival']):>5} "
            f"{r['duration_min']:>4}m {r['changes']:>2}  {price:>8}  {r['trains']}"
        )
        if r["messages"]:
            print(f"{'':>22}  ! {r['messages']}")


def print_offers(payload: dict[str, Any]) -> None:
    clusters = ((payload.get("angebote") or {}).get("angebotsCluster")) or []
    if not clusters:
        print("no offers returned")
        return
    for cluster in clusters:
        for sub in cluster.get("angebotsSubCluster") or []:
            for pos in sub.get("angebotsPositionen") or []:
                einf = pos.get("einfacheFahrt") or {}
                for variant in ("standard", "crosssell"):
                    block = einf.get(variant)
                    if not block:
                        continue
                    rp = (block.get("reisePosition") or {}).get("reisePosition") or {}
                    if not rp.get("name"):
                        continue
                    preis = (rp.get("preis") or {}).get("betrag")
                    streich = (((rp.get("streichpreis") or {}).get("preis")) or {}).get("betrag")
                    kat = (block.get("reisePosition") or {}).get("lupKategorien") or {}
                    ctx = (block.get("reisePosition") or {}).get("angebotsKontext") or {}
                    label = f"{rp.get('name')} [{variant}]"
                    money = "-" if preis is None else f"{preis:.2f} EUR"
                    if streich:
                        money += f" (statt {streich:.2f})"
                    print(f"{label:<34} {money:<22} art={kat.get('angebotsArt')} angebotsId={ctx.get('angebotsId')}")


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def _add_pax_options(s: argparse.ArgumentParser) -> None:
    s.add_argument("--class", dest="klasse", default="KLASSE_2", choices=["KLASSE_1", "KLASSE_2"])
    s.add_argument("--pax", type=int, default=1, help="number of adults (default 1)")
    s.add_argument(
        "--bahncard",
        default=None,
        choices=["25", "50", "100"],
        help="BahnCard discount -> sends 'BAHNCARD<n> KLASSE_<x>'",
    )
    s.add_argument(
        "--ermaessigung",
        action="append",
        default=[],
        metavar="KEY",
        help='raw discount key, e.g. "BAHNCARD25 KLASSE_2" or "KEINE_ERMAESSIGUNG KLASSENLOS"',
    )
    s.add_argument(
        "--child",
        type=int,
        action="append",
        default=[],
        metavar="AGE",
        help="add a child of this age (JUGENDLICHER, repeatable)",
    )


def _travellers_from_args(args: argparse.Namespace) -> list[dict[str, Any]]:
    return build_travellers(
        pax=args.pax,
        bahncard=args.bahncard,
        klasse=args.klasse,
        extra=args.ermaessigung,
        children=args.child,
    )


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="DB Navigator HAFAS API client")
    p.add_argument("--json", action="store_true", help="dump raw JSON")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("station", help="search stations")
    s.add_argument("term")

    s = sub.add_parser("search", help="connection search with prices")
    s.add_argument("from_station")
    s.add_argument("to_station")
    s.add_argument("--at", default=None, help="YYYY-MM-DDTHH:MM (default: now+1h)")
    s.add_argument("--max-changes", type=int, default=None)
    s.add_argument("--context", default=None, help="frueherContext/spaeterContext for paging")
    _add_pax_options(s)

    s = sub.add_parser("offers", help="priced offer details for one connection")
    s.add_argument("from_station")
    s.add_argument("to_station")
    s.add_argument("--at", default=None)
    s.add_argument("--index", type=int, default=0)
    _add_pax_options(s)

    s = sub.add_parser("bestprice", help="best price per 3h slice for one day")
    s.add_argument("from_station")
    s.add_argument("to_station")
    s.add_argument("--day", default=None, help="YYYY-MM-DD (default: today)")
    _add_pax_options(s)

    s = sub.add_parser("departures", help="live departure board")
    s.add_argument("station")
    s.add_argument("--day", default=None)

    args = p.parse_args(argv)

    if args.cmd == "station":
        hits = search_stations(args.term)
        if args.json:
            print(json.dumps(hits, ensure_ascii=False, indent=1))
        else:
            for h in hits:
                print(f"{h.get('evaNr','?'):>8}  {h.get('name')}  {h.get('locationId')}")
        return 0

    if args.cmd == "departures":
        st = resolve_station(args.station)
        day = datetime.fromisoformat(args.day) if args.day else datetime.now()
        data = departures(st["evaNr"], day)
        if args.json:
            print(json.dumps(data, ensure_ascii=False, indent=1))
        else:
            for d in data.get("bahnhofstafelAbfahrtPositionen", [])[:25]:
                t = (d.get("ezAbgangsDatum") or d.get("abgangsDatum") or "")[11:16]
                print(f"{t}  {d.get('mitteltext') or d.get('kurztext'):<8} {d.get('richtung') or ''}")
        return 0

    src = resolve_station(args.from_station)
    dst = resolve_station(args.to_station)
    travellers = _travellers_from_args(args)

    if args.cmd == "search":
        when = datetime.fromisoformat(args.at) if args.at else datetime.now() + timedelta(hours=1)
        data = search_connections(
            src["locationId"], dst["locationId"], when,
            klasse=args.klasse, travellers=travellers,
            max_changes=args.max_changes, context=args.context,
        )
        if args.json:
            print(json.dumps(data, ensure_ascii=False, indent=1))
        else:
            print_rows(connection_rows(data))
        return 0

    if args.cmd == "offers":
        when = datetime.fromisoformat(args.at) if args.at else datetime.now() + timedelta(hours=1)
        data = search_connections(
            src["locationId"], dst["locationId"], when,
            klasse=args.klasse, travellers=travellers,
        )
        conns = [i["verbindung"] for i in data.get("verbindungen", [])]
        if not conns:
            raise SystemExit("no connections")
        offers = connection_offers(
            conns[min(args.index, len(conns) - 1)],
            klasse=args.klasse,
            travellers=travellers,
        )
        if args.json:
            print(json.dumps(offers, ensure_ascii=False, indent=1))
        else:
            print_offers(offers)
        return 0

    if args.cmd == "bestprice":
        day = datetime.fromisoformat(args.day) if args.day else datetime.now()
        data = day_best_prices(
            src["locationId"], dst["locationId"], day,
            klasse=args.klasse, travellers=travellers,
        )
        if args.json:
            print(json.dumps(data, ensure_ascii=False, indent=1))
        else:
            for iv in data.get("tagesbestPreisIntervalle", []):
                start = iv["intervallAb"][11:16]
                end = iv["intervallBis"][11:16] if iv["intervallBis"][11:19] != "00:00:00" else "24:00"
                price = (iv.get("angebotsPreis") or {}).get("betrag")
                flag = "  <== Tagesbestpreis" if iv.get("istBestpreis") else ""
                print(f"{start}-{end}  {'-' if price is None else f'{price:7.2f} EUR'}{flag}")
        return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())
