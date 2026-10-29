---
name: secondhand-bulk-lot-sourcing
description: "Use when sourcing cheap bulk/Konvolut lots on classifieds."
---

# Secondhand Bulk-Lot Sourcing (Kiloware / Konvolut / Job Lots)

Finds **quantity-priced secondhand lots** — collections, Konvolute, Kiloware, Teilepakete,
job lots — instead of single products/sets, and normalizes them to a comparable unit price
(€/kg, €/1000 parts, €/Stück). Built and verified on Kleinanzeigen (09/2026), applicable to
any classifieds source.

## When to Use

- User asks for "billige Sammlung / Konvolut / Einzelteile / Kiloware / Bulk / Lots" on a
  classifieds market, or says "mit denen man X bauen könnte" (parts basis for a MOC/project).
- User wants a **cheap lot as raw material**, not a specific model/set.
- User wants to know whether a bundle is cheaper than the sum of singles.

Not for: finding one specific product/model (use the dedicated product-search skill), or
bidding/negotiating (use the negotiation skill).

## Hard Rules

1. **Never search the target product.** "Cheap lots to build X" searches bulk *vocabulary*;
   searching X returns only finished sets. Two passes: (a) keyword pass with bulk vocabulary,
   (b) category sweep with `max_price` over all pages — the value is in the client-side
   filtering, not the keywords.
2. **Unit price only from plausible candidates.** Collect ALL weight/quantity candidates,
   test each against a plausibility band, keep the plausible one; if none fits, report the
   quantity as **unknown — never guess**. A single naive regex produces absurd €/kg and
   silently reorders the whole ranking.
3. **Per-kilo listings are already unit prices.** "Preis je Kilo / pro Kilo / Kilopreis /
   /kg" → the price field IS €/kg. Never divide again; list these separately.
4. **Shipping/pickup must be read from the ad itself.** A page-wide string test is
   false-positive (related-ads widgets and JSON-LD contain "Versand möglich"). If the ad is
   silent, write "nicht angegeben → klären".
5. **Every outgoing link is verified before it is shown.** Rebuild the output table from the
   stored dataset, then fetch each link and match title+price. Links reconstructed from
   memory/earlier output resolve to *unrelated* ads without any error (silent 200).
6. **Separate the raw-material story from the technical story.** Big lots give structural
   parts cheaply, but specials (pneumatics, motors, RC/receiver, rare elements) essentially
   never appear in kilo lots — surface those as their own leads/sources instead of pretending
   the lot covers the build.
7. **Be honest about feasibility.** If the finished product is cheaper than the parts mix,
   say so plainly (with price anchors) instead of recommending a worse build path.

## Procedure

1. **Parse intent.** Target product/goal, nearest plausible unit (kg? parts? sets?), radius,
   budget ceiling, and whether pickup is realistic (distance from the user's home).
2. **Generate bulk vocabulary** (German market): `konvolut, sammlung, einzelteile, kiloware,
   teilepaket, teilekonvolut, schuettware, restposten, restbestand, gemischt, wuerfelkiste,
   kiste, sortiment, "nach gewicht", "je kilo", kg, kilo, grundbausteine, "viele teile",
   "grosse menge"` + brand terms. 20–35 keywords, run with `size=100`, pages 0–1, dedupe by
   ad id.
3. **Category sweep** for the local case: `category_id` of the parent category (LEGO has no
   own subcategory — use Spielzeug), `location_id` + `distance` (50 and 100 km), `max_price`,
   `poster_type=None`, `include_top_ads=True`, all pages. This finds "nur Abholung" bargains
   that keyword search misses.
4. **Filter client-side.** Keep lots (bulk word in title/description), drop other-brand/
   non-compatible, minifigure-only, instructions/catalog/stickers, "suche/tausche" ads, and
   ads whose title is a specific set number without a bulk word.
5. **Normalize prices** with the parser recipe in
   `references/kleinanzeigen_bulk_scan.md` (weight candidates → plausibility band → €/kg;
   parts count → €/1000; per-kg-listing flag).
6. **Verify the AI-selected top candidates on the ad page**: current price (search index can
   lag), condition, shipping vs pickup-only, seller's `Aktiv seit` / `<n> Anzeigen online`.
   Fetching with a browser UA + regex on `id="viewad-title"`, `id="viewad-price"`,
   `id="viewad-description-text"` works; compare title+fingerprint against the dataset.
7. **Collect the specials separately** (the bottleneck parts/motors/controllers), including
   part numbers and brand-compatible equivalents, plus the finished-product price anchors.
8. **Deliver**: cheapest-by-unit table, per-region/local section (state the empty case
   explicitly instead of padding), the specials table, price anchors, and a total-cost note
   including shipping. Attach the full list as a file for long result sets.

## Pitfalls

- **Kilopreis-Falle:** one naive `(\d+[.,]?\d*)\s*kg` match turns jokes/text fragments into
  0.1 €/kg and inverts the ranking. Always multi-candidate + band check.
- **German number formats:** "1,850 Kg" (comma-in-grams), "2,2 Kg" vs "2.2 kg"; sub-kg lots
  only give grams — include a gram fallback.
- **"Preis je Kilo" ads recur in every bulk market** (sellers offering by the kilo): mark them
  and keep them out of the total-price ranking.
- **Search index ≠ live price:** a lot can be cheaper/newer on the ad page than in the search
  hit (and `data-soldlabel` is template noise, not a sold indicator).
- **Dealer parts-list ads:** the price field shows the *cheapest single part* while the text
  carries a price list — treat as a parts source, not as a cheap product.
- **Aggregate/near-duplicate ads:** one seller with several similar lots (different weights,
  same text) is common; keep them together as one seller profile rather than three "deals".
- **Pickup-only outliers dominate €/kg rankings:** always show the distance and the pickup
  constraint next to the €/kg, otherwise the "best" lot is unusable.
- **A thin regional market is a valid finding.** Report "no local supply, here's the
  nationwide + shipping path" instead of lowering quality standards to fill a local list.

## Verification

- Re-fetch every published link; require title match and matching price string.
- Cross-check the collected count against the number of queries/pages run (dedupe drift).
- State the scan date and that prices/shipping were read live on that date.
- Recompute €/kg for the 3–5 headline items by hand from the ad text as a sanity check.

## References

- `references/kleinanzeigen_bulk_scan.md` — concrete Kleinanzeigen recipe: API calls,
  category/location IDs, weight-parser code, shipping/pickup detection, link verification.
- `references/brick_moc_part_sourcing.md` — domain knowledge bank for brick/Technic MOCs:
  used-bulk price bands, LEGO Pneumatic V2 part numbers, Mould King model/price anchors,
  what a multi-thousand-part MOC actually needs.
