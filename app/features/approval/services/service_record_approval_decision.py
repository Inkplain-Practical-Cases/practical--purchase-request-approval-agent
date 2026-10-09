# Only an authorized human decision may finish a pending purchase request.
from fastapi import HTTPException
from app.providers.dependencies import get_purchase_store
from app.features.approval.services.service_authorize_approver import service_authorize_approver
from app.features.approval.schemas.manager_decision import ManagerDecision

def service_record_approval_decision(request_id:int, manager_id:str, decision:ManagerDecision)->dict:
    store=get_purchase_store()
    request=store.get(request_id)
    if request is None:
        raise HTTPException(status_code=404,detail="Purchase request not found")
    service_authorize_approver(manager_id,request["requester_id"])
    target="approved" if decision.action=="approve" else "rejected"
    try:
        return store.transition(request_id,target,actor=manager_id,reason=decision.reason)
    except ValueError as exc:
        raise HTTPException(status_code=409,detail="Approval is no longer pending") from exc
