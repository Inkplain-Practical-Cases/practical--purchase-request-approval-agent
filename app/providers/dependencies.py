# Dependency factory shares state in one process, not between workers.
from functools import lru_cache
from app.providers.purchase_store.in_memory_purchase_store import InMemoryPurchaseStore

@lru_cache(maxsize=1)
def get_purchase_store() -> InMemoryPurchaseStore:
    return InMemoryPurchaseStore()
