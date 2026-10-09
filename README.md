# STEP-6 — Harden and verify

A **real runnable FastAPI purchasing workflow** with validated employee requests, an inclusive €500 policy, versioned state history, manager credential verification, explicit approve/reject actions, optimistic concurrency protection and safe event logging.

```bash
python -m pip install -r requirements.txt
python -m pytest -q
uvicorn app.main:app --reload
```

POST /purchase-requests accepts request fields, including amount_eur as a decimal string. <= €500 is auto-approved; > €500 waits in pending_approval. GET /purchase-requests/{id} reads current state and transition history. For a > €500 request, POST /purchase-requests/{id}/decision with Authorization: Bearer local-demo-manager-token and JSON `{"action":"approve","reason":"Budget reviewed","expected_version":1}` to resume a pending workflow.

**Security:** The default demo manager token is for offline learning, NOT production authorization. The in-memory state is ephemeral and safe only inside one process. For real deployments, use organizational identity, per-request authorization, durable transactions, idempotency keys, audit retention and TLS.
