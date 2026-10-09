# Called inside provider's lock to avoid a check-then-update race.
from app.features.workflow_state.errors.version_conflict_error import VersionConflictError

def service_check_state_version(actual:int,expected:int|None)->None:
    if expected is not None and actual!=expected:
        raise VersionConflictError("Stale purchase request version")
