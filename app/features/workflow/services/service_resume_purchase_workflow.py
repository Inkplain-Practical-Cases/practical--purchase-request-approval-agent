# Resume a suspended workflow only after a verified manager decision.
# Store transition checks pending status and expected version under the same RLock.
from app.features.approval.schemas.manager_decision import ManagerDecision
from app.providers.dependencies import get_purchase_store

def service_resume_purchase_workflow(request_id:int,manager_id:str,decision:ManagerDecision)->dict:
    destination="approved" if decision.action=="approve" else "rejected"
    return get_purchase_store().transition(
        request_id,destination,actor=manager_id,reason=decision.reason,
        expected_version=decision.expected_version,
    )
