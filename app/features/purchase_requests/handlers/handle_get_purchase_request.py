# Safe query handler to inspect current state and audit history.
from fastapi import HTTPException
from app.providers.dependencies import get_purchase_store

def handle_get_purchase_request(identifier:int)->dict:
    found=get_purchase_store().get(identifier)
    if found is None:
        raise HTTPException(status_code=404,detail="Purchase request not found")
    return found
