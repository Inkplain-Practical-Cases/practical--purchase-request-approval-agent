# Central transition policy: terminal states cannot be reopened.
from app.features.workflow_state.schemas.purchase_state import PurchaseState

ALLOWED = {
    PurchaseState.DRAFT: {PurchaseState.APPROVED, PurchaseState.PENDING_APPROVAL, PurchaseState.REJECTED},
    PurchaseState.PENDING_APPROVAL: {PurchaseState.APPROVED, PurchaseState.REJECTED},
    PurchaseState.APPROVED: set(),
    PurchaseState.REJECTED: set(),
}

def service_transition_purchase_state(current: str, requested: str) -> None:
    old, new = PurchaseState(current), PurchaseState(requested)
    if new not in ALLOWED[old]:
        raise ValueError(f"Illegal transition: {old.value} -> {new.value}")
