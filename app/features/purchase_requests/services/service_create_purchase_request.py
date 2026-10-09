# Policy decides whether to approve or await a separate human action.
from app.features.purchase_requests.schemas.request_input import PurchaseRequestInput
from app.providers.dependencies import get_purchase_store
from app.core.config import get_auto_approval_limit
from app.features.purchase_policy.services.service_evaluate_purchase_policy import service_evaluate_purchase_policy

def service_create_purchase_request(payload: PurchaseRequestInput) -> dict:
    store = get_purchase_store()
    draft = store.create(payload)
    route = service_evaluate_purchase_policy(payload.amount_eur,get_auto_approval_limit())
    return store.transition(draft["id"],route.value,actor="system:policy",reason="initial policy route")
