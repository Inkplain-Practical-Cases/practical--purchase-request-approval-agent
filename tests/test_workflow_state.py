# State history and illegal transitions are enforced atomically by store.
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.providers.dependencies import get_purchase_store

client=TestClient(app)
BASE={"item":"Laptop","quantity":1,"amount_eur":"900.00",
      "justification":"Needed for research team","requester_id":"worker-12"}

def test_pending_history():
    data=client.post("/purchase-requests",json=BASE).json()
    assert data["status"]=="pending_approval"
    assert data["version"]==1
    assert data["history"][0]["from"]=="draft"
    assert data["history"][0]["actor"]=="system:policy"

def test_cannot_approve_terminal_status():
    request=client.post("/purchase-requests",json={**BASE,"amount_eur":"250.00"}).json()
    assert request["status"]=="approved"
    with pytest.raises(ValueError,match="Illegal transition"):
        get_purchase_store().transition(request["id"],"draft","manager-1","illegal")
