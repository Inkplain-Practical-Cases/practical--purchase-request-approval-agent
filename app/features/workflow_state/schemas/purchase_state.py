# Explicit finite states; only listed transitions can occur.
from enum import Enum

class PurchaseState(str, Enum):
    DRAFT = "draft"
    PENDING_APPROVAL = "pending_approval"
    APPROVED = "approved"
    REJECTED = "rejected"
