# Public self-hosted deployment verification

When a web app is exposed through a reverse proxy, compare the public domain with the local port and confirm both return the same build fingerprint and behavior. Identify whether the proxy targets a development server (source changes appear immediately) or a production server/build.

For a no-cloud requirement, verify the local server persistence/API path instead of requesting SaaS credentials. Two tabs can prove UI signaling but not cross-device persistence; test separate browser contexts through the public domain and inspect API/server state.
