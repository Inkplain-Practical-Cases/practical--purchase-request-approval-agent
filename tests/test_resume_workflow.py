# Validate stale/duplicate decisions with real HTTP and version checks.
from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
BASE={"item":"Workstations","quantity":2,"amount_eur":"1800.00",
      "justification":"Needed for production onboarding","requester_id":"employee-1"}
HEAD={"Authorization":"Bearer local-demo-manager-token"}

def submit():
    response=client.post("/purchase-requests",json=BASE)
    assert response.status_code==201
    return response.json()

def decide(identifier,action,version):
    return client.post(f"/purchase-requests/{identifier}/decision",headers=HEAD,
        json={"action":action,"reason":"Reviewed purchase","expected_version":version})

def test_resume_after_manager_approval():
    request=submit()
    assert request["status"]=="pending_approval"
    response=decide(request["id"],"approve",request["version"])
    assert response.status_code==200
    assert response.json()["version"]==2
    assert response.json()["status"]=="approved"

def test_duplicate_manager_decision_is_conflict():
    request=submit()
    assert decide(request["id"],"reject",request["version"]).status_code==200
    assert decide(request["id"],"reject",request["version"]).status_code==409

def test_wrong_version_does_not_modify_state():
    request=submit()
    assert decide(request["id"],"approve",0).status_code==409
    assert decide(request["id"],"approve",request["version"]).status_code==200
