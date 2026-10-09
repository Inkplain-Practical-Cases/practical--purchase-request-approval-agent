# Typed manager action: no status value can be supplied directly.
from typing import Literal
from pydantic import BaseModel,Field,ConfigDict

class ManagerDecision(BaseModel):
    model_config=ConfigDict(extra="forbid")
    action: Literal["approve","reject"]
    reason: str=Field(min_length=3,max_length=500)
