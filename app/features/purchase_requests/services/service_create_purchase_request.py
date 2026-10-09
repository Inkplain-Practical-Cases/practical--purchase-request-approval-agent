# Intake service creates a draft; later steps add policy and workflow state.
from app.features.purchase_requests.schemas.request_input import PurchaseRequestInput
from app.providers.dependencies import get_purchase_store

def service_create_purchase_request(payload: PurchaseRequestInput) -> dict:
    return get_purchase_store().create(payload)
