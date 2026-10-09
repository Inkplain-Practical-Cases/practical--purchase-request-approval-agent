# One-process data store; each guarded state change is atomic under RLock.
from threading import RLock
from app.features.purchase_requests.schemas.request_input import PurchaseRequestInput
from app.features.workflow_state.services.service_transition_purchase_state import service_transition_purchase_state

class InMemoryPurchaseStore:
    def __init__(self) -> None:
        self._records: dict[int, dict] = {}
        self._lock = RLock()
        self._next_id = 1

    def create(self, payload: PurchaseRequestInput) -> dict:
        with self._lock:
            identifier = self._next_id
            self._next_id += 1
            record = {"id":identifier, **payload.model_dump(mode="json"), "status":"draft",
                      "version":0, "history":[]}
            self._records[identifier] = record
            return self.get(identifier)

    def get(self, identifier: int) -> dict | None:
        with self._lock:
            value = self._records.get(identifier)
            return self._clone(value) if value is not None else None

    def _clone(self, value: dict) -> dict:
        return {**value, "history":[dict(event) for event in value["history"]]}

    def transition(self, identifier: int, new_state: str, actor: str, reason: str) -> dict:
        with self._lock:
            value = self._records[identifier]
            service_transition_purchase_state(value["status"],new_state)
            previous = value["status"]
            value["status"] = new_state
            value["version"] += 1
            value["history"].append({"from":previous,"to":new_state,"actor":actor,"reason":reason,
                                     "version":value["version"]})
            return self._clone(value)
