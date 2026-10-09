# Orchestration handler delegates to a validation-ready service.
from app.features.purchase_requests.schemas.request_input import PurchaseRequestInput
from app.features.purchase_requests.services.service_create_purchase_request import service_create_purchase_request

def handle_create_purchase_request(payload: PurchaseRequestInput) -> dict:
    return service_create_purchase_request(payload)
