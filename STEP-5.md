# Step 5 of 6 — Resume suspended workflows
## What you build
Version-aware manager decisions, atomic resume from pending_approval to approved/rejected, duplicate decision protection.
## What you learn
Optimistic concurrency, versioned state updates and separating authorization from state transitions.
## What changed
Three new components. The store, manager decision schema, and approval service now support versioned resume.
## Run
```bash
python -m pip install -r requirements.txt
python -m pytest -q
```
## Verify
Pending→approved, duplicated decision→409, outdated version→409 without mutation.
## Diagram
STEP-5.crd is the complete step snapshot; Simulator rendering is a later stage.
## Next
Expand audit and error coverage and finalize CI.
