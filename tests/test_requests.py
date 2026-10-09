# Real FastAPI TestClient verifies HTTP validation, not just Python models.
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
PAYLOAD = {"item": "Monitor", "quantity": 3, "amount_eur": "900.00",
           "justification": "Required for engineering productivity", "requester_id": "employee-1"}

def test_create_draft():
    result = client.post("/purchase-requests", json=PAYLOAD)
    assert result.status_code == 201
    assert result.json()["status"] == "draft"
    assert result.json()["id"] == 1

def test_invalid_payloads():
    for patch in [{"quantity": 0}, {"amount_eur": "-1"}, {"justification": ""}, {"unexpected": 1}]:
        result = client.post("/purchase-requests", json={**PAYLOAD, **patch})
        assert result.status_code == 422
