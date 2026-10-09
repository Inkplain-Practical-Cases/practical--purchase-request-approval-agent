# Thread-safe in-memory request provider. Process restart loses all records.
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

    def set_status(self, identifier: int, status: str) -> dict:
        with self._lock:
            record = self._records[identifier]
            record["status"] = status
            return dict(record)
