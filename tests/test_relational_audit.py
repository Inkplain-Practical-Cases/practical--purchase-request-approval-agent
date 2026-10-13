"""Validate SQLite purchase HTTP request and event parent relation."""
import sqlite3
from app.providers.provider_record_request_audit import provider_record_request_audit
def test_purchase_audit(tmp_path):
    db=str(tmp_path/"purchase.sqlite3")
    rid=provider_record_request_audit("POST","/purchase",200,4.1,db)
    with sqlite3.connect(db) as conn:
        assert conn.execute("SELECT COUNT(*) FROM purchase_api_requests WHERE id=?",(rid,)).fetchone()[0]==1
        assert conn.execute("SELECT COUNT(*) FROM purchase_api_events WHERE request_id=?",(rid,)).fetchone()[0]==1
        assert conn.execute("PRAGMA foreign_key_check").fetchall()==[]
