# Buying used hardware on classifieds (PC parts / SSD / RAM)

Companion to the umbrella's evidence rules. Everything here was measured live on
Kleinanzeigen in Sept/Oct 2026 during a 1 TB M.2-SSD hunt for a mini-PC.

## 1. Fit first, price second
Never rank hardware offers before checking the **target machine**:

| Check | Command | Why it decides the shortlist |
|---|---|---|
| Free RAM slot / rank / part number | `sudo dmidecode -t memory \| grep -E "Locator\|Size\|Type\|Speed\|Rank\|Part Number"` | Buy the **same rank** (1Rx8 ↔ 1Rx8); a matched module in the free slot gives dual-channel for ~20 € |
| Bus / interface | `lspci -nn \| grep -i nvme`, board specs | Gen4 SSD on a PCIe 3.0 x4 board = wasted premium; **M.2-SATA (B+M key) does not run in an NVMe M-key slot at all** |
| Worn? | `sudo smartctl -a /dev/nvme0 \| grep -E "Percentage Used\|Available Spare\|Data Units\|Power On Hours\|Temperature"` | Decides *capacity vs speed*: healthy drive + full disk ⇒ buy capacity only |
| Thermals | SMART temperature sensors | Sensor 2 can read 25–30 °C hotter than sensor 1 — tight mini-PC chassis warrant a thermal pad |
| Missing tool | `sudo apt-get install -y nvme-cli` → `nvme list` | Model/serial/firmware/namespace usage |

**If the machine you are asked about is the host you run on (`hostname`), run these yourself.**
Observed correction, verbatim: *"das kannst du lokal selbst nachschauen, du läufst auf dem
ziel rechner."* Full procedure: skill `linux-disk-space-triage`.

## 2. Retail anchor before judging used prices
Fetch the cheapest **new** price for the same spec before calling anything a deal (DE: Geizhals;
`web_extract` works, direct `curl` returns HTTP 403; the `?fs=…&sort=p&v=l&pagesize=100` list is
already price-ascending, price regex `\[€ ([\d.]+,\d{2})\]`).
Measured 09/2026 for 1 TB M.2 NVMe: cheapest new = **115 €** (Verbatim Vi3000), mainstream
134–140 € (Kingston NV3 134,90 €) — because NAND prices had spiked, the whole used market
(mostly 90–120 €) was genuinely below new, and 75–85 € was a real 26–35 % saving.
Rule: a used offer **above** current new price is a mispurchase, no matter how good it looks.

## 3. "Cheaper?" ⇒ prove exhaustion
Combine **category scan + keyword union**, then enumerate *every* candidate below the threshold
with its disqualification reason, and report the pipeline counts. Measured for 1 TB M.2:
496 ads (category scan, 5 pages) + ~600 keyword hits = **1,085 ads → 332 genuine 1 TB M.2
candidates → only 6 under 76 €**:

| Price | Why it failed |
|---|---|
| 40 € | "1TB SATA M.2" — SATA, does not run in the NVMe slot |
| 49 € | bulk ad "Verschiedene M.2 NVMe (4TB…)" — placeholder price, text said ~100 €/TB |
| 49 € | Fanxiang — only 512 GB despite "2x = 1TB" in the title |
| 50 € | Intel 660p 1 TB — fits, but *pickup only, 620 km away* |
| 58 € | Intenso "M.2 SSD TOP" — SATA-M.2 (B+M key) |
| 75 € | Rayson 1 TB "neuwertig" — valid candidate |

**Cross-check obligation:** re-run the filter *looser* (positive criterion only, no exclusion
regex) and diff. If the exclusions swallow real hits, "nothing cheaper exists" is wrong.

## 4. API notes for PC-parts scans (Kleinanzeigen)
- **Category 225 = "PC-Zubehör & Software"** — every PC-part ad carries `-225-` in its URL.
  Sweep: `api.search(q='', category_id=225, max_price=<X>, include_top_ads=True, size=100,
  count=100, page=0..N)` → 5 pages = 496 ads at 80 €.
- **`get_categories()` parsing quirk:** nodes use the **hyphenated** keys
  `localized-name.value` plus `id`; children are a list under `category`. A walker looking for
  `name` / `localizedName` returns **0 categories with no error** — a silent failure that looks
  like "no categories exist".
- Sellers often run **multiple listings from one account** (e.g. one 80 € single drive + one
  "assorted M.2 from 49 €" ad at the same ZIP) — treat placeholder prices ("Preise liegen bei
  ungefähr 100 EUR pro TB") as not-a-price.

## 5. Traps that only show up in the advert photo or full description
- **Model line ≠ interface:** Intenso **"M.2 SSD TOP" = SATA-M.2** (the NVMe line is
  "PREMIUM"); WD Blue 3D (SATA) vs WD Blue SN (NVMe). Fix: pull `og:image` from the ad page
  (`re.search(r'og:image"[^>]*content="([^"]+)"')`, load the URL **without** appending
  `?rule=` again) and let vision read the label — "M.2 SSD TOP", B+M keying and a missing
  "NVMe/PCIe" marking are unambiguous.
- A "1000 GB SSD Festplatte" cheapie was a **2.5" SATA drive**; "M2" appeared only in the
  description ("bin auf eine M2 gewechselt"). Require the form factor in the **title** plus the
  full text, and keep an exclusion regex for 2.5"/3.5"/USB/external/enclosure/adapter.
- "Zustand: 100 %" in the ad title is not evidence — demand a **CrystalDiskInfo screenshot**
  (health %, TBW, power-on hours). A candidate with *fewer* hours/TBW than the drive already
  installed in the buyer's machine is a verifiable buying argument; unknown history is a blind
  purchase and belongs flagged as such, not recommended.
- **"PayPal an Freunde" = no buyer protection.** Either pickup in person or "Waren &
  Dienstleistungen". "Sicher bezahlen" is often not offered at all on private listings.
- Warranty reality: private sales are usually "keine Garantie, keine Rücknahme" — factor that
  into the price gap versus new.

## 6. Reporting shape that worked
Rank by *value incl. risk*, not by price alone, and keep a separate line for traps: a table of
verified-live offers (price, model, location, shipping/payment, SMART evidence), then the
observed price drops since the last run (sellers cut prices without notifying anyone —
re-read the ad page, don't trust the search index), then an explicit "do not buy" list with
reasons. Close with the retail anchor so the saving is quantified.
