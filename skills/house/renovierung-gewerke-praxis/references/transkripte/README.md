# Transkripte der Top-Fehler-Videos

15 Videos, alle am 09.11.2026 abgerufen, Untertitel per `yt-dlp` (automatische Untertitel, `de`),
mit einem eigenen Parser entdoppelt (rollende Captions) und in Absätze à 20 s mit `[hh:mm:ss]` geschnitten.
**ASR-Qualität:** Wörter können falsch erkannt sein („Bartsanierung" = Badsanierung, „Strich" = Estrich,
„Kwattstunden" = Kilowattstunden). Zitate daraus sind Hörbelege, keine Bildbelege — in den Playbooks
entsprechend markiert.

| Datei | Kanal | Titel | Länge | Datum | URL |
|---|---|---|---|---|---|
| `BjwRSuspdiA.txt` | Fertighausexperte | Die 10 teuersten Fehler bei Hausbau und Sanierung | 33:50 | 22.04.2024 | https://www.youtube.com/watch?v=BjwRSuspdiA |
| `nulK-nz67Cc.txt` | Fertighausexperte | Die 20 größten Fehler beim Hausbau! | 52:43 | 08.02.2022 | https://www.youtube.com/watch?v=nulK-nz67Cc |
| `sWXyiNADbFk.txt` | Spiel und Zeug | Unsere Haussanierung: 12 Fehler, die ich bereue | 17:55 | 30.05.2026 | https://www.youtube.com/watch?v=sWXyiNADbFk |
| `k3q49IW19KU.txt` | Johannes / Flipper Immo | FEHLER BEIM RENOVIEREN – Das würde ich nie wieder machen | 16:09 | 19.01.2025 | https://www.youtube.com/watch?v=k3q49IW19KU |
| `TszegjPc69w.txt` | schlau energiesparen | 9 teure Dämm-Fehler | 18:26 | 06.04.2025 | https://www.youtube.com/watch?v=TszegjPc69w |
| `dW-Sf-yaEBQ.txt` | Step by Step Elektro | Schwerer Elektro Pfusch Teil 1 | 6:03 | 25.01.2023 | https://www.youtube.com/watch?v=dW-Sf-yaEBQ |
| `eNpMPWvnWiI.txt` | ProofWood Technik | Fehler in Elektroinstallationen! So machst du es richtig | 17:21 | 24.01.2024 | https://www.youtube.com/watch?v=eNpMPWvnWiI |
| `zR7LyRq3G7Q.txt` | Der Fliesenleger | Die 5 GRÖßTEN FEHLER bei einer BADSANIERUNG | 21:53 | 05.04.2026 | https://www.youtube.com/watch?v=zR7LyRq3G7Q |
| `3tVsWxStiL0.txt` | MrHandwerk | VERMEIDE diese FEHLER beim Fliesen verlegen | 10:31 | 23.11.2023 | https://www.youtube.com/watch?v=3tVsWxStiL0 |
| `wnWCWCQfkvg.txt` | Estrich Werke Süddeutschland | 5 Estrich Fehler die du vermeiden solltest | 05:30 | 12.02.2025 | https://www.youtube.com/watch?v=wnWCWCQfkvg |
| `85lc2Wgwyqc.txt` | schlau energiesparen | 5 Wärmepumpen Fehler die richtig teuer werden | 06:14 | 02.04.2023 | https://www.youtube.com/watch?v=85lc2Wgwyqc |
| `E-XkG-ColoU.txt` | Grün Aufgedeckt | Was Dein Heizungsbauer bei der Wärmepumpe im Altbau Verschweigt | 13:55 | 03.09.2026 | https://www.youtube.com/watch?v=E-XkG-ColoU |
| `jZoqWtTPq1U.txt` | Photovoltaik mit Philipp | PV Speicher Größe: DAS sagt dir Niemand! | 21:59 | 10.04.2026 | https://www.youtube.com/watch?v=jZoqWtTPq1U |
| `BP_WFJ6155E.txt` | Machs Dir Selbst Solar | Dein Solarteur plant zu klein: Der Wechselrichter-Fehler, den keiner anspricht | 23:45 | 17.10.2026 | https://www.youtube.com/watch?v=BP_WFJ6155E |
| `ZuOYSxy21wg.txt` | Freunde des Stroms | Schlimmer Fehler im Altbau – Elektrik im Altbau. Lebensgefährlich! | 15:16 | 10.12.2023 | https://www.youtube.com/watch?v=ZuOYSxy21wg |

Zusammen **4:41 h Video, 51.291 Wörter** Transkript. Jeder Fehler daraus ist als Testfall in
`../fehlerkatalog.json` erfasst und wird mit `../../scripts/fehlercheck.py` gegen die Wissensbasis geprüft.

**Die fünf am 09.11.2026 ergänzten Videos** (Wärmepumpe/Ölheizung, PV/Speicher/Wallbox, Elektro im Altbau)
tragen die Katalog-IDs `85lc2Wgwyqc-nn`, `E-XkG-ColoU-nn`, `jZoqWtTPq1U-nn`, `BP_WFJ6155E-nn` und
`ZuOYSxy21wg-nn` (29 Fehler). Auswahlkriterium war die Aufrufzahl im Thema, nicht die Kanalgröße:
680.033 (Elektrik Altbau), 286.297 (Speichergröße), 94.250 (Wechselrichter), 41.388 (WP-Fehler),
37.473 (WP im Altbau). Jedes Zitat im Katalog ist gegen die hier liegende Textdatei geprüft; die Zeitmarke
ist der Absatz, in dem das Zitat steht (±20 s), nicht die sekundengenaue Stelle.
