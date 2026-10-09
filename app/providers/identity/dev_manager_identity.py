# Local demonstration credential only, never use as a production identity provider.
# Credential comparisons happen on the server, not from request body role claims.
import os
from hmac import compare_digest
from fastapi import HTTPException

def dev_manager_identity(authorization: str | None) -> str:
    expected=os.getenv("DEMO_MANAGER_TOKEN","local-demo-manager-token")
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401,detail="Manager authentication required")
    if not compare_digest(authorization[7:],expected):
        raise HTTPException(status_code=401,detail="Invalid manager credentials")
    return "manager-1"
