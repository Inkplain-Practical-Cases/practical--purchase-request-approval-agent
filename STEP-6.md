# Step 6 of 6 — Harden and verify
## What you build
Final real FastAPI approval workflow with authenticated manager decisions, GET state history, concurrent decision guards and safe structured audit logging.
## What you learn
HTTP and workflow error contracts, thread-safe transition guards, non-sensitive audit logs, and end-to-end pytest.
## What changed since step 5
Adds read endpoint and audit events; evolves purchase/approval services.
## Run
```bash
python -m pip install -r requirements.txt
python -m pytest -q
uvicorn app.main:app --reload
```
## Verify
Automatic approval, human approve/reject, stale version conflict, simultaneous contradictory manager decisions, missing auth, and safe audit output.
## Diagram
STEP-6.crd is the final step's cumulative architecture; main receives FINAL.crd. Six-tab Simulator belongs to Stage 3 only.
## Next
Use FINAL.crd for Simulator visualization after explicit authorization.
