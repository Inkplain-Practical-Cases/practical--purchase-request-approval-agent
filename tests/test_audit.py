# Observability must not emit manager token or private purchasing rationale.
import json
import logging
from app.core.observability import service_log_approval_event

def test_structured_audit_is_safe(caplog):
    with caplog.at_level(logging.INFO,logger="northstar.purchase"):
        service_log_approval_event("human_decision_completed",43,"approved",2)
    assert json.loads(caplog.records[-1].message)=={
        "event":"human_decision_completed","request_id":43,"state":"approved","version":2}
    assert "token" not in caplog.records[-1].message
