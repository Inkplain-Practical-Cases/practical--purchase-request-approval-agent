# Full HTTP workflow: policy, manager review, audit and final state.
import json
from concurrent.futures import ThreadPoolExecutor
from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
BASE={"item":"Engineering monitors","quantity":3,"amount_eur":"900.00",
      "justification":"Required for the engineering team's workspace","requester_id":"worker-17"}
HEAD={"Authorization":"Bearer local-demo-manager-token"}

def create(amount="900.00",requester="worker-17"):
    result=client.post("/purchase-requests",json={**BASE,"amount_eur":amount,"requester_id":requester})
    assert result.status_code==201
    return result.json()

def decide(req,action="approve",version=None):
    if version is None: version=req["version"]
    return client.post(f"/purchase-requests/{req['id']}/decision",headers=HEAD,
                       json={"action":action,"reason":"Budget reviewed","expected_version":version})

def test_complete_auto_approval():
    result=create(amount="500.00")
    assert result["status"]=="approved"
    queried=client.get(f"/purchase-requests/{result['id']}")
    assert queried.status_code==200
    assert queried.json()["history"][0]["actor"]=="system:policy"

def test_complete_human_approval_and_rejection():
    approved=create()
    assert approved["status"]=="pending_approval"
    assert decide(approved).json()["status"]=="approved"
    rejected=create()
    assert decide(rejected,"reject").json()["status"]=="rejected"
    assert client.get(f"/purchase-requests/{rejected['id']}").json()["history"][-1]["actor"]=="manager-1"

def test_two_simultaneous_manager_decisions_one_wins():
    pending=create()
    with ThreadPoolExecutor(max_workers=2) as pool:
        futures=[pool.submit(decide,pending,choice) for choice in ("approve","reject")]
        responses=[future.result() for future in futures]
    assert sorted(response.status_code for response in responses)==[200,409]
    final=client.get(f"/purchase-requests/{pending['id']}").json()
    assert final["version"]==2
    assert len(final["history"])==2

def test_denied_and_unknown_request():
    pending=create()
    assert client.post(f"/purchase-requests/{pending['id']}/decision",
                       json={"action":"approve","reason":"No credential"}).status_code==401
    assert client.get("/purchase-requests/99999").status_code==404
