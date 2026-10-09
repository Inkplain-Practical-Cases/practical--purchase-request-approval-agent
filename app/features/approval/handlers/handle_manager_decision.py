# HTTP handler delegates authenticated actions to the decision service.
from app.features.approval.schemas.manager_decision import ManagerDecision
from app.features.approval.services.service_record_approval_decision import service_record_approval_decision

def handle_manager_decision(request_id:int, manager_id:str, decision:ManagerDecision)->dict:
    return service_record_approval_decision(request_id,manager_id,decision)
