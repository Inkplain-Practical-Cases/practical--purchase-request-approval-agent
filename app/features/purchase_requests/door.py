# Thin HTTP door: all behavior belongs to handlers and services.
from fastapi import APIRouter, status
from app.features.purchase_requests.schemas.request_input import PurchaseRequestInput
from app.features.purchase_requests.handlers.handle_create_purchase_request import handle_create_purchase_request
router = APIRouter(prefix="/purchase-requests", tags=["Purchase requests"])

@router.post("", status_code=status.HTTP_201_CREATED)
def create_purchase_request(payload: PurchaseRequestInput) -> dict:
    return handle_create_purchase_request(payload)
