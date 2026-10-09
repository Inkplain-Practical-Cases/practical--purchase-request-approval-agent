# Versioned resume logs outcome metadata without sensitive request contents.
from app.features.approval.schemas.manager_decision import ManagerDecision
from app.providers.dependencies import get_purchase_store
from app.core.observability import service_log_approval_event

def service_resume_purchase_workflow(request_id:int,manager_id:str,decision:ManagerDecision)->dict:
    target="approved" if decision.action=="approve" else "rejected"
    result=get_purchase_store().transition(
        request_id,target,actor=manager_id,reason=decision.reason,
        expected_version=decision.expected_version,
    )
    service_log_approval_event("human_decision_completed",request_id,result["status"],result["version"])
    return result
