# Step 4 of 6 — Add human approval
## What you build
A manager-only HTTP endpoint that accepts only approve/reject and writes a reasoned decision to history.
## What you learn
HITL trust boundary, credential verification, self-approval prohibition and prevention of decisions on final states.
## What changed since STEP-3
Six authorization/approval components. app/main.py includes a new HTTP door.
## Run
```bash
python -m pip install -r requirements.txt
python -m pytest -q
```
## Verify
A manager may approve or reject only pending requests. Missing credentials 401; requester approving own purchase 403; acting on terminal state 409.
## Diagram
STEP-4.crd records the human decision components. Stage 3 draws this tab.
## Next
Separate human decision intake from resuming the suspended workflow, and add version guards.
