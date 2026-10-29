# Kleinanzeigen automation playbook

Use only after explicit user authorization for automated outreach.

## State and deduplication

- Load account conversations before searching or sending.
- Use the listing/ad ID as the primary duplicate key.
- Persist conversation ID and the last handled seller-message ID.
- Save state atomically after every mutation.
- Use a process lock so overlapping cron runs cannot send duplicates.
- Add a delay between multiple sends.

## Dry-run and filtering

Run a dry-run against live results before enabling mutations. For PS5 Pro, require the title itself to indicate a console, such as `Konsole`, `Console`, `2 TB`, `Disc-Laufwerk`, or `Digital`. Reject monitor, SSD, controller-only, accessory, defective, repair, wanted, trade, and sold listings even when the description contains “PS5 Pro”. Script-only watchdogs must emit nothing on no-change; diagnostics belong on stderr.

## Example buying policy (PS5 Pro)

- Maximum total/listing price: 900 €.
- Initial offer: no more than 10% below the listing price.
- Pickup: only within 25 km of the search location; weekday evenings or weekends.
- Shipping: Kleinanzeigen “Sicher bezahlen” or PayPal Goods & Services only.
- Never bank transfer or PayPal Friends.
- Seller replies may be answered and negotiated automatically when explicitly authorized, never above 900 €.
