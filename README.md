# Purchase Request Approval Agent

Beginner FDE practical case for Northstar Operations: receive equipment/software purchasing requests, validate fields, evaluate configurable spending policies, auto-approve compliant requests up to EUR 500, pause higher-amount requests for manager approval, enforce server-side approver authorization, persist explicit workflow state and decision history, resume safely after a human decision and test invalid transitions and duplicate approvals. Educational mock purchasing workflow; not a live enterprise procurement integration.

An Inkplain practical case: a real project built step by step.

## How this repository works

Every step of the lesson has its own branch, and each one contains all steps up to it:

```bash
git clone https://github.com/Inkplain-Practical-Cases/practical--purchase-request-approval-agent.git
cd practical--purchase-request-approval-agent
git branch -r            # list the step branches
git checkout step-01-…   # code after step 1
```

`main` holds the final, complete version.
