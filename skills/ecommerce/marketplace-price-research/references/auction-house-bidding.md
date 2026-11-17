# Auction houses (Shopify/Webkul) — reading live auctions and judging a bid

Companion to the umbrella's evidence rules. Applies when the user points at an auction shop
(one item per lot, 1 € start, no reserve, countdown) instead of a fixed-price listing, or shares
a social "deal" link that turns out to be a vendor account.

## 1. From a shared link to the actual source
- Reddit share URLs `/u/<user>/s/<id>` resolve on load to the real post; the profile's own post
  list is often hidden ("likes to keep their posts hidden"), so read the profile bio — the vendor
  domain is usually there. Social "deal" posts are normally self-promotion: skip the post, work
  on the shop.
- `web_extract` refuses reddit.com share/shortener URLs; the browser resolves them fine.
- Identify the shopware underneath before scraping: Shopify + the Webkul *Shopify Auction* app
  (`sp-auction.webkul.com` assets) is the common combination for EU server/hardware auctions.

## 2. Enumerating lots: the grid, not the API
- `GET /products.json?limit=250&page=N` is the fast way to get titles/handles/variant ids, but it
  carries **no auction state**: a variant price of `0.00` only means "no bid yet". Sitemap
  endpoints may return empty; do not conclude the shop has no inventory.
- Bid state is rendered client-side by a widget (`<div id="wk-auction" prod-id=…>`) fed by the
  app, so read the **rendered DOM**, not the product HTML.
- Grid listing: `/collections/all-products?sort_by=auction_date-ascending` renders per card
  `NNd : NNh : NNm : NNs`, `No. of Bids: n`, `Current Bid: EUR x`.
- **Not-yet-live lots also render a countdown**, prefixed `Auction Starts In`. Classify on the
  label, never on "a countdown exists" — otherwise upcoming lots pollute the live list and their
  empty bid counts read as bargains.
- Parse into `{title, ends_at, bids, current_bid, url}` and persist to JSON before filtering; a
  full sweep of a few hundred lots is one page and is worth re-reading later for price movement.

## 3. Per-lot truth lives in the product page
Rendered product page text carries `Bid End Date <dd Mon yyyy HH:MM TZ>`, `Current Bid EUR x`,
`n Bid(s)`, `Minimum bidding EUR y`. The **Product Specifications** table is where the condition
is stated and it decides the value:

| Field | Why it changes the price ceiling |
|---|---|
| `Condition` | Used/refurbished — no commercial warranty unless the text says so |
| `Health` | Enterprise SSD/HDD endurance %. 70–79 % is usable but must be priced below 90–100 % |
| `Capacity` + form factor | 2.5" SAS/U.2 vs 3.5" SATA decides whether the buyer's chassis can even take it |
| `Included Railkit` / `no CPU/RAM/disks` | A barebone minus rails, caddies, CPU, RAM is not the price of a working server |
| `HDD Form Factor` + model family | SMR families (e.g. Ultrastar HC680) are unsuitable for NAS/RAID rebuilds — say so |

## 4. Economics that decide whether "1 €" is a deal
- Hammer prices are **excl. VAT**; DE adds 19 % (OSS). Quote netto and brutto, or at minimum say
  the VAT is missing from the displayed figure.
- Shipping is quoted only after login/checkout and depends on weight/size class: a 1U server or a
  5U JBOD can add more than the lot itself; RAM sticks/SFP modules are cheap to ship. Never call a
  heavy lot cheap before the shipping class is known — say explicitly that it is unknown.
- Bids are binding and non-retractable; popcorn bidding extends the end by ~1 min per last-minute
  bid; and many shops block consecutive bids by the same account, so the working move is a
  **proxy bid with a hard maximum**, not manual re-bidding.
- EU-only shipping, no warranty, 14-day withdrawal with return shipping on the buyer. Factor a
  risk buffer, larger for low `Health` and for barebones.

## 5. Judging the list, not the price tag
- Visible prices on lots with days left are €1-increment noise: 1 bid / 1 € after six days says
  nothing about the outcome. Rank by **value ceiling vs. time left**, then watch.
- Lots ending within ~24 h with dozens of bids are already priced in — the classic pattern is a
  multi-drive SSD lot bid to ~per-unit market price after 40+ bids. Say so instead of listing it
  as a bargain.
- Enterprise parts rarely have usable sold data: fall back to reseller/parts-shop list prices
  (servermall, bargainhardware, itinstock, serversupply, PCPartWatch) and label them as asking
  prices, matching on exact part number and new-vs-used basis.
- Compute the ceiling per lot: market reference minus VAT, minus expected shipping, minus risk
  buffer for health/condition. Report lots that still have headroom, not lots that merely look
  cheap today.

## 6. Reporting shape that worked
A compact table `Artikel | Stand (Gebot/Gebote) | Ende | Realität (Marktreferenz)` for the few
lots with headroom, then one line of "already too hot" lots with the reason, then the platform
caveats (VAT, unknown shipping, no warranty, binding bids) and the concrete next action. Keep it
short — the user asked "gute Angebote?", not for a market report.
