# Public deployment verification

Use this checklist after delegated implementation work when a public URL is available.

1. Probe the public URL directly with `curl -fsSI` and extract visible landing-page text.
2. Treat HTTP 200, TLS, server headers, and landing-page text as **reachability/rendering** evidence only.
3. Test the actual user flow separately: create a room, open the room URL in two independent browser sessions, join, vote, and observe the match/presence behavior.
4. For Supabase, verify the configured environment and exercise persistence plus Realtime. Without credentials or a live configured backend, mark API/Realtime as **not verified**, even if the local fallback works.
5. Compare the deployed asset/content with the intended local changes; a live site may be an older deployment and can pass a smoke test while missing new data or code.

Recommended report labels: Passed, Failed, Not verified, Not implemented.