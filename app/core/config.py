# Currency threshold is configurable without editing workflow code.
import os
from decimal import Decimal

def get_auto_approval_limit() -> Decimal:
    value = Decimal(os.getenv("AUTO_APPROVAL_LIMIT_EUR", "500.00"))
    if value < 0:
        raise ValueError("AUTO_APPROVAL_LIMIT_EUR must not be negative")
    return value
