# STEP-4 — Human approval
Run `python -m pip install -r requirements.txt && python -m pytest -q`.

POST /purchase-requests/{id}/decision with Authorization: Bearer local-demo-manager-token and body `{ "action":"approve", "reason":"Manager approved" }` for a pending request. The token is a local demonstration fixture; real production authorization requires verified users, access control, TLS, and organizational policy. Missing/incorrect credentials return 401, self approval 403, stale decisions 409.
