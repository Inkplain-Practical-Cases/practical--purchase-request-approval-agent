# STEP-3 — Explicit workflow state
Run `python -m pip install -r requirements.txt && python -m pytest -q`.

Each valid request moves from draft to either approved or pending_approval, preserving a versioned history entry. Terminal states cannot move backwards. The state check and record update are atomic under one process-local RLock. This is not durable or multi-worker safe.
