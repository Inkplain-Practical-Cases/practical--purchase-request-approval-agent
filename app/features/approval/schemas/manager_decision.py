# A manager may choose an action, not directly set arbitrary workflow state.
from typing import Literal
from pydantic import BaseModel,Field,ConfigDict

class ManagerDecision(BaseModel):
    model_config=ConfigDict(extra="forbid")
    action: Literal["approve","reject"]
    reason: str=Field(min_length=3,max_length=500)
    # Optional for compatibility with STEP-4; supplying it guards stale views.
    expected_version: int|None=Field(default=None,ge=0)
