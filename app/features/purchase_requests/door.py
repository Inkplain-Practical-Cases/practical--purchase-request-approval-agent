# Thin HTTP router; handlers and services own procurement logic.
from fastapi import APIRouter,status
from app.features.purchase_requests.schemas.request_input import PurchaseRequestInput
from app.features.purchase_requests.handlers.handle_create_purchase_request import handle_create_purchase_request
from app.features.purchase_requests.handlers.handle_get_purchase_request import handle_get_purchase_request
router=APIRouter(prefix="/purchase-requests",tags=["Purchase requests"])

@router.post("",status_code=status.HTTP_201_CREATED)
def create_purchase_request(payload:PurchaseRequestInput)->dict:
    return handle_create_purchase_request(payload)

@router.get("/{identifier}")
def get_purchase_request(identifier:int)->dict:
    return handle_get_purchase_request(identifier)
