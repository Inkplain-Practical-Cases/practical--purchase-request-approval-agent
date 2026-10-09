# Real HTTP route tests protect the approval trust boundary.
from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
P={"item":"Monitors","quantity":3,"amount_eur":"900.00",
   "justification":"Required for engineering team","requester_id":"employee-1"}
HEAD={"Authorization":"Bearer local-demo-manager-token"}

def new_request(requester="employee-1",amount="900.00"):
    return client.post("/purchase-requests",json={**P,"requester_id":requester,"amount_eur":amount}).json()

def test_manager_can_approve_pending():
    request=new_request()
    result=client.post(f"/purchase-requests/{request['id']}/decision",
        headers=HEAD,json={"action":"approve","reason":"Required equipment"})
    assert result.status_code==200
    assert result.json()["status"]=="approved"
    assert result.json()["history"][-1]["actor"]=="manager-1"

def test_manager_can_reject_pending():
    request=new_request()
    result=client.post(f"/purchase-requests/{request['id']}/decision",
        headers=HEAD,json={"action":"reject","reason":"Budget unavailable"})
    assert result.status_code==200
    assert result.json()["status"]=="rejected"

def test_rejects_unauthenticated_and_self_approval():
    request=new_request()
    assert client.post(f"/purchase-requests/{request['id']}/decision",
        json={"action":"approve","reason":"Looks good"}).status_code==401
    other=new_request(requester="manager-1")
    assert client.post(f"/purchase-requests/{other['id']}/decision",
        headers=HEAD,json={"action":"approve","reason":"Self request"}).status_code==403

def test_terminal_state_cannot_be_changed():
    auto=new_request(amount="250.00")
    assert client.post(f"/purchase-requests/{auto['id']}/decision",
        headers=HEAD,json={"action":"reject","reason":"Try to override"}).status_code==409
