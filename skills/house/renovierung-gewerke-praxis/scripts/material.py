#!/usr/bin/env python3
"""Rechenwerkzeug für die Renovierung — Mengen, U-Werte, Heizlast, Kosten.

Jede Formel nennt ihre Herkunft. Wo der Faktor eine Setzung ist, steht [SETZUNG] dabei:
das ist ein Erfahrungswert, kein belegter Normwert, und darf nicht als Beleg zitiert werden.

Aufruf:
    python3 material.py fliesen --flaeche 25 --preis 45
    python3 material.py ausgleich --flaeche 12 --mm 5
    python3 material.py farbe --flaeche 60 --ergiebigkeit 10 --anstriche 2
    python3 material.py u-wert --u-alt 1.5 --dicke 160 --lambda 0.035
    python3 material.py heizlast --oel-liter 2500
    python3 material.py estrich --flaeche 80 --dicke 6
    python3 material.py selftest
"""
from __future__ import annotations

import argparse
import math
import sys

R_SI = 0.13   # Wärmeübergangswiderstand innen, DIN EN ISO 6946
R_SE = 0.04   # außen, DIN EN ISO 6946


def fliesen(flaeche: float, verschnitt: float = 10.0, preis_m2: float = 0.0,
            pro_packung: float = 1.44) -> dict:
    """Fliesenmenge inkl. Verschnitt.

    verschnitt: 10 % bei gerader Verlegung, 15 % diagonal — Erfahrungswert [SETZUNG],
    deckt sich mit den Herstellerangaben in references/playbooks/fliesen.md.
    """
    netto = flaeche * (1 + verschnitt / 100)
    packungen = math.ceil(netto / pro_packung) if pro_packung else None
    out = {
        "flaeche_m2": round(flaeche, 2),
        "verschnitt_pct": verschnitt,
        "bestellmenge_m2": round(netto, 2),
        "packungen": packungen,
        "material_eur": round(netto * preis_m2, 2) if preis_m2 else None,
    }
    return out


def ausgleich(flaeche: float, mm: float, kg_pro_mm: float = 1.6, sack_kg: float = 25.0) -> dict:
    """Ausgleichsmasse: Verbrauch je mm Schichtdicke.

    kg_pro_mm 1,6 kg/(m²·mm) ist der übliche Herstellerwert für zementäre Ausgleichsmasse
    [SETZUNG, herstellerabhängig 1,5–1,7]; Fliestrich 1,7–1,8.
    """
    kg = flaeche * mm * kg_pro_mm
    return {
        "flaeche_m2": round(flaeche, 2),
        "dicke_mm": mm,
        "kg": round(kg, 1),
        "saecke_25kg": math.ceil(kg / sack_kg),
        "hinweis": "Grundierung und Randdämmstreifen separat kalkulieren",
    }


def farbe(flaeche: float, ergiebigkeit: float = 10.0, anstriche: int = 2,
          gebinde_l: float = 12.5) -> dict:
    """Farbmenge. ergiebigkeit = m² je Liter und Anstrich (steht auf dem Eimer)."""
    liter = flaeche * anstriche / ergiebigkeit
    return {
        "flaeche_m2": round(flaeche, 2),
        "anstriche": anstriche,
        "liter": round(liter, 2),
        "gebinde": math.ceil(liter / gebinde_l),
    }


def u_wert(u_alt: float, dicke_mm: float, lambda_wlz: float) -> dict:
    """U-Wert einer zusätzlichen Dämm Lage, ohne die alte Wand zu kennen.

    R = d/λ; der zusätzliche Widerstand senkt den U-Wert nach
        1/U_neu = 1/U_alt + R_zusatz      (DIN EN ISO 6946, Reihenschaltung)
    Gilt nur, wenn die Dämmung ungestört und vollflächig ist; Wärmebrücken der
    Befestigung sind hier NICHT enthalten (Tellerdübel kosten 0,01–0,03 W/(m²K)).
    """
    r_zusatz = (dicke_mm / 1000) / lambda_wlz
    u_neu = 1 / (1 / u_alt + r_zusatz)
    return {
        "u_alt": u_alt,
        "dicke_mm": dicke_mm,
        "lambda": lambda_wlz,
        "r_zusatz": round(r_zusatz, 2),
        "u_neu": round(u_neu, 3),
        "verbesserung_pct": round((1 - u_neu / u_alt) * 100, 1),
        "hinweis": "ohne Dübel-Wärmebrücken und ohne Fensterlaibungen gerechnet",
    }


def heizlast(oel_liter: float, nutzungsgrad: float = 0.80, volllaststunden: float = 2000.0,
             heizwert_kwh_l: float = 10.0) -> dict:
    """Heizlast aus dem Ölverbrauch — der einzige verbrauchsbasierte Weg ohne Wärmebild.

    Formel: Q = Liter × Heizwert × Nutzungsgrad; P = Q / Volllaststunden.
    Nutzungsgrad 0,80 für einen 20+ Jahre alten Kessel [SETZUNG], 0,90–0,95 für Brennwert.
    Volllaststunden 2.000 h/a ist die übliche Annahme für Wohngebäude [SETZUNG];
    der Skill nennt 1.800–2.200 h.
    Ergebnis ist ein Überschlag — für die Geräteauswahl gilt DIN EN 12831 (raumweise).
    """
    q_kwh = oel_liter * heizwert_kwh_l * nutzungsgrad
    p_kw = q_kwh / volllaststunden
    strom_kwh = q_kwh / 3.0   # JAZ 3,0 als Rechenwert
    return {
        "oel_liter": oel_liter,
        "nutzungsgrad": nutzungsgrad,
        "waermebedarf_kwh_a": round(q_kwh),
        "heizlast_kw": round(p_kw, 1),
        "strombedarf_kwh_a_bei_jaz3": round(strom_kwh),
        "hinweis": "Überschlag; DIN EN 12831 raumweise ist für die Auslegung maßgeblich",
    }


def estrich(flaeche: float, dicke_cm: float, kg_pro_m2_cm: float = 20.0) -> dict:
    """Estrichmaterial: Zementestrich braucht rund 20 kg/(m²·cm) Trockenmasse [SETZUNG]."""
    kg = flaeche * dicke_cm * kg_pro_m2_cm
    return {
        "flaeche_m2": round(flaeche, 2),
        "dicke_cm": dicke_cm,
        "volumen_m3": round(flaeche * dicke_cm / 100, 2),
        "trockenmasse_kg": round(kg),
        "saecke_40kg": math.ceil(kg / 40),
        "hinweis": "Bewehrung, Randdämmstreifen und Belegreife separat; 1 m³ Zementestrich ≈ 2.000 kg",
    }


def selftest() -> int:
    ok = True

    def check(name, got, want, tol=0.01):
        nonlocal ok
        good = abs(got - want) <= tol
        ok &= good
        print(f"{'ok  ' if good else 'FAIL'} {name}: {got} (erwartet {want})")

    f = fliesen(25, 10, 45)
    check("fliesen bestellmenge", f["bestellmenge_m2"], 27.5)
    check("fliesen material", f["material_eur"], 1237.5)

    a = ausgleich(12, 5)
    check("ausgleich kg", a["kg"], 96.0)
    check("ausgleich säcke", a["saecke_25kg"], 4)

    u = u_wert(1.5, 160, 0.035)
    check("u-wert 16 cm WLZ035 auf 1,5", u["u_neu"], 0.19, 0.01)

    h = heizlast(2500)
    check("heizlast 2500 l", h["heizlast_kw"], 10.0, 0.05)

    e = estrich(80, 6)
    check("estrich m3", e["volumen_m3"], 4.8)

    print("\nSelbsttest", "bestanden" if ok else "FEHLGESCHLAGEN")
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p1 = sub.add_parser("fliesen")
    p1.add_argument("--flaeche", type=float, required=True)
    p1.add_argument("--verschnitt", type=float, default=10.0)
    p1.add_argument("--preis", type=float, default=0.0)
    p1.add_argument("--pro-packung", type=float, default=1.44)

    p2 = sub.add_parser("ausgleich")
    p2.add_argument("--flaeche", type=float, required=True)
    p2.add_argument("--mm", type=float, required=True)

    p3 = sub.add_parser("farbe")
    p3.add_argument("--flaeche", type=float, required=True)
    p3.add_argument("--ergiebigkeit", type=float, default=10.0)
    p3.add_argument("--anstriche", type=int, default=2)

    p4 = sub.add_parser("u-wert")
    p4.add_argument("--u-alt", type=float, required=True)
    p4.add_argument("--dicke", type=float, required=True)
    p4.add_argument("--lambda", dest="lambda_", type=float, required=True)

    p5 = sub.add_parser("heizlast")
    p5.add_argument("--oel-liter", type=float, required=True)
    p5.add_argument("--nutzungsgrad", type=float, default=0.80)

    p6 = sub.add_parser("estrich")
    p6.add_argument("--flaeche", type=float, required=True)
    p6.add_argument("--dicke", type=float, required=True)

    sub.add_parser("selftest")

    a = ap.parse_args()
    if a.cmd == "fliesen":
        r = fliesen(a.flaeche, a.verschnitt, a.preis, a.pro_packung)
    elif a.cmd == "ausgleich":
        r = ausgleich(a.flaeche, a.mm)
    elif a.cmd == "farbe":
        r = farbe(a.flaeche, a.ergiebigkeit, a.anstriche)
    elif a.cmd == "u-wert":
        r = u_wert(a.u_alt, a.dicke, a.lambda_)
    elif a.cmd == "heizlast":
        r = heizlast(a.oel_liter, a.nutzungsgrad)
    elif a.cmd == "estrich":
        r = estrich(a.flaeche, a.dicke)
    else:
        return selftest()

    for key, value in r.items():
        print(f"{key:<28} {value}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
