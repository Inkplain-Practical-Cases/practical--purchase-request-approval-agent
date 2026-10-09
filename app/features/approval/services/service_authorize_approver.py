# Server-side separation of duties: a requester must not approve themselves.
from fastapi import HTTPException

def service_authorize_approver(manager_id: str, requester_id: str) -> None:
    if manager_id==requester_id:
        raise HTTPException(status_code=403,detail="Self-approval forbidden")
