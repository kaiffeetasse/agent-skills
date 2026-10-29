# Kleinanzeigen: Scam-Risiko, Abholung und Zahlungsbedingungen

## Bewertungsroutine

Bewerte Abholung, realistische Erreichbarkeit, Vor-Ort-Prüfung, Plattformzahlung, Verkäuferbereitschaft zur geschützten Zahlung und Profil-/Bewertungssignale getrennt. **Abholung ist ein positives Signal, aber kein Betrugsnachweis und keine Entwarnung.** Prüfe den Ort gegen die tatsächliche Entfernung des Käufers; „Abholung möglich“ aus 700 km Entfernung ist kein praktikabler Schutz.

Eine Plattform-API kann „Sicher bezahlen“ technisch anbieten, obwohl der Verkäufer es ablehnt. Für Versand zählt deshalb beides: API-Verfügbarkeit UND ausdrückliche Bereitschaft des Verkäufers. „Nur PayPal Freunde“ oder Überweisung bedeutet: keinen Versand auf dieser Basis. Profilalter, frühere Anzeigen oder ein angebotenes Ausweisfoto heben diese Regel nicht auf.

## Bestehende Chats: Pflicht vor einer Empfehlung

1. Hole `get_conversation(conv_id)` frisch; die Konversationsübersicht ist nur ein Pointer, nicht der ganze Verlauf.
2. Ordne jede Nachricht nach Richtung, Autor, Typ und Zeit ein. Systemereignisse („Bezahlung angefragt“) sind keine Verkäuferzustimmung.
3. Lies den kompletten Verlauf und erkenne Bedingungen in einer scheinbaren Zusage: „Preis ok, Abholung passt; Versand nur PayPal Freunde“ ist keine Zusage zu geschütztem Versand.
4. Prüfe `paymentStatusBar`, `paymentStateSummary`, `paymentAnalyticsData` und `get_conversation_payment_status()`. Sage ausdrücklich, ob nur ein Angebot aussteht, ob Zahlung möglich ist oder ob tatsächlich bezahlt wurde. „Bezahlung angefragt“ bedeutet **nicht bezahlen**.
5. Prüfe den letzten eigenen Text auf falsche Implikationen. Wenn er Versand/Zahlungslink anfordert, obwohl geschützter Versand nicht vereinbart wurde, keine weitere verbindliche Bestätigung und keinen externen Zahlungslink anfordern. Klarstellen, nicht zahlen, bevor geschützter In-App-Zahlungsweg aktiv und Verkäuferzustimmung eindeutig ist.

## Reputation und Belege kalibrieren

- Anzeigen-Score, öffentliches Profil und Reputation-Endpunkt können voneinander abweichen. Bei fehlenden/widersprüchlichen Werten als „nicht verifiziert“ beschreiben, nicht als gute Bewertung auslegen.
- Account-Alter und historische Anzeigen sind positive, aber keine entscheidenden Signale; Konten können übernommen werden.
- Eine Ausweiskopie ist weder Echtheits- noch Käuferschutzbeleg. Keine Ausweis-, Telefonnummer- oder Zahlungsdaten außerhalb des offiziellen Ablaufs teilen.
- Bilder können Produkt und Zubehör plausibel zeigen, beweisen aber Besitz/Echtheit nicht. Sichtbare Rechnung/Seriennummer nicht als vorhanden werten, wenn sie auf den Bildern nicht lesbar ist.
- Einen sehr niedrigen Paketpreis als Prüfbedarf nennen, nicht allein als Scam-Beweis. Idealerweise separat gegen aktuelle vergleichbare Komponenten/Bundlepreise prüfen.

## Ausgabe an Nutzer

Trenne **beobachtete Fakten** von **Risikoeinschätzung** und gib ein kalibriertes Urteil („Risiko erhöht“, „nicht eindeutig“, „keine sichere Entwarnung“), keine kategorische Betrugsbehauptung ohne Beleg. Sage, welcher Zahlungsweg akzeptabel ist, ob Vor-Ort-Test praktikabel ist, ob bereits ein aktives Angebot besteht und ob jetzt gezahlt werden darf. Keine Nachricht selbst senden oder Kaufangebot ändern, sofern nicht ausdrücklich beauftragt.

## Reproduktionsfall: PS5-Pro-Bundle Fehmarn (09/2026)

- Listing/API: private Anzeige, 570 € VB, 18 Bilder, PS5 Pro + zusätzliche 2-TB-NVMe, Disc-Laufwerk, Edge-Controller und Zubehör; Rechnungs-/Funktionsangaben in Text. Ort 23769 Fehmarn, rund 700 km vom Suchenden entfernt.
- Profil: Konto seit 2011, 2.879 historische Anzeigen; Profil zeigte Ratingwert 0,95, Reputation-Endpunkt lieferte 0 Bewertungen. Schluss: Historie positives Signal, Rating nicht verifiziert.
- Versand: API bot Hermes/DHL und sicheren Zahlungsflow; bei 570 € ergab sich 603,14 € Gesamtpreis. Verkäufer schrieb aber „Bei Versand nur Paypal F&F“. Technische Verfügbarkeit bedeutet nicht Zustimmung.
- Chat: Verkäufer „Ok, ich stimme zu“ bezog sich auf den Preis, aber Versandbedingung war F&F. Nach der Abholfrage bestätigte er Abholung, wiederholte aber F&F-only bei Versand. Der letzte eigene Text „machen wir es bei 455 € fest … Zahlungslink bzw. Versanddaten“ war deshalb missverständlich.
- Live-Plattformstatus: echtes Kaufangebot 455 €, 48,297 € Gesamt inkl. Hermes und Gebühr; Status „Bezahlung angefragt — Zahle noch nicht“. Käufer darf nicht daraus ableiten, dass Verkäufer geschützten Versand akzeptiert oder dass eine Zahlung fällig ist.
- Lehre: Abholung allein entwarnt nicht; sichere API-Zahlung allein entwarnt ebenfalls nicht. Ein Preis-„OK“ löst Zahlungsbedingung nicht. Bei unpraktikabler Fernabholung plus F&F-only Versand keine sichere Empfehlung zum Versandkauf.
