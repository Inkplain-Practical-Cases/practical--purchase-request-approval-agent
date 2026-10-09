# Step 3 of 6 — Implement workflow state
## What you build
An explicit transition table, versioned state updates and history inside one locked provider.
## What you learn
draft→approved/pending, pending→approved/rejected, and rejecting illegal terminal changes. The transition guard and mutation share a lock.
## What changed
PurchaseState and service_transition_purchase_state added. The store and intake service now use transition instead of raw set_status.
## Run
```bash
python -m pip install -r requirements.txt
python -m pytest -q
```
## Verify
Tests show a history record for draft→pending and rejection of approved→draft.
## Diagram
STEP-3.crd describes all current source-level components. Stage 3 will visualize it.
## Next
Implement authenticated human manager decisions.
