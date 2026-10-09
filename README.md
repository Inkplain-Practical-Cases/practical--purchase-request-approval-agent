# Purchase Request Approval Agent — STEP-1
A runnable FastAPI request-intake API following Inkplain Codebase Structure (door → handler → service → provider).

```bash
python -m pip install -r requirements.txt
python -m pytest -q
uvicorn app.main:app --reload
```

Visit http://127.0.0.1:8000/docs and POST /purchase-requests with item, quantity, amount_eur, justification and requester_id. A valid request is stored as draft. This version intentionally does not apply a purchase policy yet; no real buying takes place.
