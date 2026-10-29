---
name: marketplace-price-research
description: "Use for price research. Separate asking and sold prices."
version: 1.0.0
author: Hermes Agent
license: MIT
category: ecommerce
tags: [price-research, marketplaces, ebay, kleinanzeigen, bricklink, collectibles, valuation]
metadata:
  hermes:
    related_skills: [ebay-search, kleinanzeigen-search, flip-research, collectible-valuation]
---

# Marketplace Price Research

Use this class-level skill whenever a user asks what an item is worth, requests comparison prices, wants sold/completed marketplace evidence, or compares buying on classifieds with reselling on a marketplace.

## Evidence hierarchy

Keep evidence types separate throughout the workflow:

1. **Realized sales** — completed transactions or a source explicitly reporting historical sales.
2. **Active marketplace listings** — current asking prices, not proof of sale.
3. **Classifieds asking prices** — usually private-sale expectations and negotiation anchors.
4. **Catalog/reference facts** — identity, year, parts, variants; not price evidence.

Never merge these into one undifferentiated price range. Every reported price must carry its source and evidence type.

## Workflow

1. Identify the exact item, model/set number, variant, condition, completeness, packaging, and relevant reissue numbers.
2. Generate precise queries and synonyms, but filter before computing statistics. Exclude accessories, spare parts, bundles, sibling models, wanted ads, rebuilds, €1 placeholders, and obvious dreamer prices unless the user explicitly wants them.
3. Search local classifieds using the available API, aggregate across query variants, deduplicate by listing ID and identical description/text, and preserve canonical links.
4. Search active eBay listings read-only with a real browser session (`curl` on `ebay.de/sch/...` returns only the JS challenge page). Parse client-rendered cards by walking `a[href*="/itm/"]` + `closest('li').innerText` (class names like `li.s-item` change), retain listing ID/title/price/shipping/condition/link, strip tracking parameters, and label every result as active asking price. **A price shown as "EUR 39,99 / EUR 38,79 mit Gutscheincode X" is conditional** — report both numbers plus the code and its expiry, never the discounted figure alone.
5. For realized prices, test whether the source actually exposes historical sales. eBay.de anonymous `LH_Sold=1&LH_Complete=1` searches may redirect to login; if so, stop retrying the same route. Do not invent sold results and do not call active listings sold.
6. Select an appropriate realized-price source: BrickLink price guides for LEGO/collectibles, Discogs release-level data for music, or a genuinely authenticated marketplace history. Keep new/sealed and used/incomplete populations separate.
7. Compute median and quartiles for comparable prices. Prefer median and monthly/typical clusters over mean; report sample size, range, and notable outliers. For small samples, say that the statistic is weak.
8. For margin analysis, subtract purchase price, shipping, platform fees, expected repair/parts costs, and a risk buffer. Show gross versus estimated net margin and state assumptions.
9. Report raw comparables first, then a condition-specific price window and one actionable next step. German requests should receive concise German output unless the user asks otherwise.

## eBay sold-listing rule

A sold filter is useful only if the page returns actual completed-item data. A login page, generic error page, HTTP 403, or empty result set is not sold evidence. In that case say “eBay-Sold-Daten anonym nicht zugänglich” and use a supported realized-price source or report only active asking prices.

## Quality and safety

- Read-only by default: never bid, buy, message sellers, or alter watchlists without explicit confirmation.
- Do not expose tokens, cookies, account credentials, or private browser state.
- Use source URLs returned by the source; never fabricate listing links.
- Distinguish item price, shipping, fees, and total cost.
- Preserve raw result data when doing multi-item research so counts and deduplication can be verified.

## Support references

- `references/ebay-sold-access.md` — tested interpretation of eBay sold-search responses and fallback decision tree.

## Related skills

This umbrella overlaps with narrower `ebay-search`, `kleinanzeigen-search`, `flip-research`, and `collectible-valuation` skills. Use their source-specific recipes when available, but apply this skill's evidence-labeling rules first.
