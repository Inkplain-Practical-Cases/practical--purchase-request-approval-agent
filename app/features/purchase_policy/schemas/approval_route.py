# The policy chooses a route, never impersonates a human approver.
from enum import Enum

class ApprovalRoute(str, Enum):
    AUTO_APPROVED = "approved"
    MANAGER_REVIEW = "pending_approval"
