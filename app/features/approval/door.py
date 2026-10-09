# Authenticated approval door — never trust a user-submitted "manager" role.
from fastapi import APIRouter,Header
from app.providers.identity.dev_manager_identity import dev_manager_identity
from app.features.approval.schemas.manager_decision import ManagerDecision
from app.features.approval.handlers.handle_manager_decision import handle_manager_decision
router=APIRouter(prefix="/purchase-requests",tags=["Manager approval"])

@router.post("/{request_id}/decision")
def decide_purchase_request(request_id:int, decision:ManagerDecision,
                            authorization:str|None=Header(default=None))->dict:
    manager_id=dev_manager_identity(authorization)
    return handle_manager_decision(request_id,manager_id,decision)
