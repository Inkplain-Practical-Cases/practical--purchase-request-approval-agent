# Thread-safe demo store; not durable, not suitable for multiple workers.
from threading import RLock
from app.features.purchase_requests.schemas.request_input import PurchaseRequestInput

class InMemoryPurchaseStore:
    def __init__(self) -> None:
        self._records: dict[int, dict] = {}
        self._lock = RLock()
        self._next_id = 1

    def create(self, payload: PurchaseRequestInput) -> dict:
        with self._lock:
            identifier = self._next_id
            self._next_id += 1
            record = {"id": identifier, **payload.model_dump(mode="json"), "status": "draft"}
            self._records[identifier] = record
            return dict(record)

    def get(self, identifier: int) -> dict | None:
        with self._lock:
            value = self._records.get(identifier)
            return dict(value) if value is not None else None
