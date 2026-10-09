# Policy boundaries and runtime configuration exercised over real HTTP.
from decimal import Decimal
from fastapi.testclient import TestClient
import pytest
from app.main import app
from app.core.config import get_auto_approval_limit
from app.features.purchase_policy.services.service_evaluate_purchase_policy import service_evaluate_purchase_policy

client = TestClient(app)
BASE={"item":"Monitor","quantity":1,"amount_eur":"250.00",
      "justification":"New engineering desk setup","requester_id":"employee-1"}

@pytest.mark.parametrize("amount,status",[("250.00","approved"),("500.00","approved"),("900.00","pending_approval")])
def test_policy_http(amount,status):
    result=client.post("/purchase-requests",json={**BASE,"amount_eur":amount})
    assert result.status_code==201
    assert result.json()["status"]==status

def test_configurable_limit(monkeypatch):
    monkeypatch.setenv("AUTO_APPROVAL_LIMIT_EUR","1000")
    assert get_auto_approval_limit()==Decimal("1000")
    result=client.post("/purchase-requests",json={**BASE,"amount_eur":"900.00"})
    assert result.json()["status"]=="approved"

def test_negative_threshold_rejected(monkeypatch):
    monkeypatch.setenv("AUTO_APPROVAL_LIMIT_EUR","-1")
    with pytest.raises(ValueError):
        get_auto_approval_limit()
