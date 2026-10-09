# Store the request, evaluate its policy route and return its stored state.
# A later step will centralize all state transitions in a single state machine.
from app.features.purchase_requests.schemas.request_input import PurchaseRequestInput
from app.providers.dependencies import get_purchase_store
from app.core.config import get_auto_approval_limit
from app.features.purchase_policy.services.service_evaluate_purchase_policy import service_evaluate_purchase_policy

def service_create_purchase_request(payload: PurchaseRequestInput) -> dict:
    store = get_purchase_store()
    created = store.create(payload)
    route = service_evaluate_purchase_policy(payload.amount_eur, get_auto_approval_limit())
    return store.set_status(created["id"], route.value)
