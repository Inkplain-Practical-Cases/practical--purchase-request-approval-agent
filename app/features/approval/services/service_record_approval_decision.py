# Manager decision is checked before resuming a previously pending workflow.
from fastapi import HTTPException
from app.providers.dependencies import get_purchase_store
from app.features.approval.services.service_authorize_approver import service_authorize_approver
from app.features.approval.schemas.manager_decision import ManagerDecision
from app.features.workflow.services.service_resume_purchase_workflow import service_resume_purchase_workflow
from app.features.workflow_state.errors.version_conflict_error import VersionConflictError

def service_record_approval_decision(request_id:int,manager_id:str,decision:ManagerDecision)->dict:
    request=get_purchase_store().get(request_id)
    if request is None:
        raise HTTPException(status_code=404,detail="Purchase request not found")
    service_authorize_approver(manager_id,request["requester_id"])
    try:
        return service_resume_purchase_workflow(request_id,manager_id,decision)
    except (ValueError,VersionConflictError) as exc:
        raise HTTPException(status_code=409,detail="Approval is stale or no longer pending") from exc
