# State changes and optimistic version checks are atomic in one process.
from threading import RLock
from app.features.purchase_requests.schemas.request_input import PurchaseRequestInput
from app.features.workflow_state.services.service_transition_purchase_state import service_transition_purchase_state
from app.features.workflow_state.services.service_check_state_version import service_check_state_version

class InMemoryPurchaseStore:
    def __init__(self)->None:
        self._records:dict[int,dict]={}
        self._lock=RLock()
        self._next_id=1

    def _clone(self,value:dict)->dict:
        return {**value,"history":[dict(event) for event in value["history"]]}

    def create(self,payload:PurchaseRequestInput)->dict:
        with self._lock:
            identifier=self._next_id
            self._next_id+=1
            record={"id":identifier,**payload.model_dump(mode="json"),"status":"draft","version":0,"history":[]}
            self._records[identifier]=record
            return self._clone(record)

    def get(self,identifier:int)->dict|None:
        with self._lock:
            value=self._records.get(identifier)
            return self._clone(value) if value is not None else None

    def transition(self,identifier:int,new_state:str,actor:str,reason:str,
                   expected_version:int|None=None)->dict:
        with self._lock:
            record=self._records[identifier]
            service_check_state_version(record["version"],expected_version)
            service_transition_purchase_state(record["status"],new_state)
            previous=record["status"]
            record["status"]=new_state
            record["version"]+=1
            record["history"].append({"from":previous,"to":new_state,"actor":actor,"reason":reason,
                                      "version":record["version"]})
            return self._clone(record)
