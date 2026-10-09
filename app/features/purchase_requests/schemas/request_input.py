# Boundary validation: invalid money, quantities, and short reasons never reach services.
from decimal import Decimal
from pydantic import BaseModel, Field, ConfigDict

class PurchaseRequestInput(BaseModel):
    model_config = ConfigDict(extra="forbid")
    item: str = Field(min_length=3, max_length=120)
    quantity: int = Field(gt=0, le=100)
    amount_eur: Decimal = Field(gt=0, max_digits=10, decimal_places=2)
    justification: str = Field(min_length=10, max_length=1000)
    requester_id: str = Field(min_length=3, max_length=80)
