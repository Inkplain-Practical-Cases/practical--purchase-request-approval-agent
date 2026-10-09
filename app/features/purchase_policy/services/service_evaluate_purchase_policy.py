# No external AI call makes a binding procurement decision.
from decimal import Decimal
from app.features.purchase_policy.schemas.approval_route import ApprovalRoute

def service_evaluate_purchase_policy(amount_eur: Decimal, threshold: Decimal) -> ApprovalRoute:
    if amount_eur <= 0:
        raise ValueError("amount_eur must be positive")
    return ApprovalRoute.AUTO_APPROVED if amount_eur <= threshold else ApprovalRoute.MANAGER_REVIEW
