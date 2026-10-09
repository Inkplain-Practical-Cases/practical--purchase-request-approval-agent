# STEP-5 — Resume suspended approval workflows
Use the FastAPI `/docs` page to create a €900 request, record the returned version, then POST a manager action to `/purchase-requests/{id}/decision` with `expected_version`. The manager credential is a local demo fixture only. The transition guard checks version and state while holding the same per-process lock. Tests reject stale versions and duplicate decisions; state/history are not durable beyond process lifetime.

Run `python -m pip install -r requirements.txt && python -m pytest -q`.
