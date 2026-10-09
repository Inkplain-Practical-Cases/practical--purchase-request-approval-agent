# Step 2 of 6 — Evaluate business rules
## What you build in this step
A deterministic purchase policy service, typed ApprovalRoute, and editable €500 threshold.
## What you learn
Separate policy evaluation from HTTP door and state provider. The policy routes an action but cannot make a human decision.
## What changed since step 1
New config, ApprovalRoute and policy service; create service and in-memory store changed.
## Run it
```bash
python -m pip install -r requirements.txt
python -m pytest -q
uvicorn app.main:app --reload
```
## Verify it
€250/€500→approved and €900→pending_approval; change AUTO_APPROVAL_LIMIT_EUR to test a different cutoff. Invalid requests still fail.
## Diagram
STEP-2.crd represents all components; Stage 3 adds a Simulator tab.
## Next
Introduce a transition-validated state machine and history.
