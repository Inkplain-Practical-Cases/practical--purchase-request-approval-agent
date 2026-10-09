# Step 1 of 6 — Receive purchase requests
## What you build in this step
Real FastAPI POST /purchase-requests, typed Pydantic validation, an in-memory draft store.
## What you learn
Input contracts, thin door, handler→service→provider delegation and HTTP response testing.
## What changed since STEP-0
Six initial components added to a standalone working slice.
## Run it
```bash
python -m pip install -r requirements.txt
python -m pytest -q
uvicorn app.main:app --reload
```
## Verify it
TestClient creates one draft with HTTP 201 and rejects bad quantities, amounts, justifications and unknown properties with HTTP 422.
## Diagram
The CRD is created from this branch. Stage 3 will draw STEP-1 in .inkp.
## Next
Policy evaluation branches by €500 threshold.
