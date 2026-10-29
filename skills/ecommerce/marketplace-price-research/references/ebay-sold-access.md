# eBay sold-search access note

Verified behavior for eBay Germany during the September 2026 Docker-Hermes session:

- Anonymous `https://www.ebay.de/sch/i.html?_nkw=<query>&LH_Sold=1&LH_Complete=1` redirected to an eBay login page with no listing cards.
- Equivalent anonymous eBay web requests could return HTTP 403 or a generic error page.
- Therefore a login page, 403, generic error, or empty card set is **not** evidence that there were no sold listings.
- Do not keep retrying the same anonymous sold URL or silently substitute active asking prices.

Fallback decision tree:

1. If an authenticated browser session is explicitly available and actually returns completed-item cards, use those cards and label them sold.
2. Otherwise use the platform's supported realized-price source: BrickLink price guide for LEGO/collectibles; Discogs release-level data for music.
3. Use eBay active listings only as asking-price context, clearly labeled `aktiv / Angebotspreis`.
4. In the final result state the limitation in one concise sentence and include the retrieval date/source.

For LEGO, BrickLink's price guide is rendered client-side. Use the set's `-1` identifier, wait for the price table, keep `Used` separate from `New`, report `Times Sold`, min/avg/max and monthly clusters, and remember that the default Used population generally represents complete sets rather than incomplete lots.
