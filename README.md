# Purchase Request Approval Agent

**Inkplain Practical Case 3/6 — Starter Forward Deployed Engineering.**

A working local FastAPI application teaches input validation, deterministic purchase policy, explicit workflow state, human approval, version-aware resumption, concurrency safety and auditable decision history. Northstar Operations is fictional: **no real purchase or payment** is made.

## Run (Python 3.12+)
```bash
git clone https://github.com/Inkplain-Practical-Cases/practical--purchase-request-approval-agent.git
cd practical--purchase-request-approval-agent
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
python -m pytest -q
uvicorn app.main:app --reload
```
Open http://127.0.0.1:8000/docs.

## Interactive workflow
1. POST `/purchase-requests`: item, quantity, amount_eur as a decimal string, justification and requester_id.
2. The service validates all fields and evaluates `AUTO_APPROVAL_LIMIT_EUR` (default 500.00, inclusive).
3. Up to €500 is approved by policy; above €500 stays `pending_approval` (human decision required).
4. GET `/purchase-requests/{id}` returns current status, version and history.
5. A manager sends POST `/purchase-requests/{id}/decision` with `Authorization: Bearer local-demo-manager-token`, `{"action":"approve","reason":"Budget reviewed","expected_version":1}`. Another valid action is `reject`.
6. Wrong/absent credentials: HTTP 401; self-approval: HTTP 403; missing request: HTTP 404; invalid state or stale version: HTTP 409. The transition and version check share a provider lock.

**Security note:** The built-in manager token is a **development fixture**, not production authentication. The identity provider always returns the demo manager after verifying the token; use a real corporate identity/authorization provider and TLS in production. The in-memory state is only for one process, not durable, not cross-worker and not suitable for financial approvals in production. User-provided requester_id is demo input, not verified authentication.

## Cumulative branches

| Step | Branch | Capability |
|---|---|---|
| 1 | step-01-receive-purchase-requests | Validated FastAPI request intake, in-memory drafts |
| 2 | step-02-evaluate-business-rules | Configurable inclusive €500 auto approval and manual routing |
| 3 | step-03-implement-workflow-state | Finite transition table, atomic state and audit history |
| 4 | step-04-add-human-approval | Server-verified demo manager decision, self-approval guard |
| 5 | step-05-resume-suspended-workflows | Version-aware suspended workflow resume and stale decision handling |
| 6 | step-06-harden-and-verify | HTTP state reading, concurrency tests and structured audit events |

Each teaching branch has `STEP-N.crd` + `STEP-N.md`, a runnable source tree and pytest. The final `main` contains `FINAL.crd` and this README. A six-tab `.inkp` Simulator belongs to **Stage 3**, and is not generated in this stage.

## Architecture — Inkplain Codebase Structure
FastAPI routes are thin **doors**. They call feature **handlers** (request intake, manager decision, read-only state), which delegate to **services** (purchase creation/policy, manager authorization, state transitions, workflow resume). The in-memory **provider** owns atomic mutations and audit history, and a distinct mock identity provider verifies the development manager token. The CRD maps all source-level components and relationships.

## Validation and tests
```bash
python -m pytest -q
```
Tests exercise real FastAPI TestClient behavior: invalid input 422, threshold boundary at €500, pending manager approval, terminal state transition denial, manager authentication, self-approval, stale/duplicate version conflicts, simultaneous decisions and audit events without sensitive request content.

CI workflow `.github/workflows/tests.yml` runs pytest against six step branches and main using a seven-entry matrix. Every branch installs its own dependency file.

## Next stages
After Stage 2 verification and explicit user approval, Stage 3 builds `purchase-request-approval-agent.inkp` from the six `STEP-N.crd` snapshots, then Stage 4 publishes learning lessons with linked real source examples.
