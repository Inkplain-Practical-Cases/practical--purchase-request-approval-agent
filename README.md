# STEP-2 — Purchase policy routing
Run `python -m pip install -r requirements.txt && python -m pytest -q`.

Create a request through `POST /purchase-requests` from the FastAPI `/docs` page. Amounts <= €500 are automatically approved; requests over €500 enter `pending_approval`. Step 2 does not provide a manager decision yet. The policy threshold is configurable by `AUTO_APPROVAL_LIMIT_EUR`; this is a demonstration rule, not real procurement policy.
