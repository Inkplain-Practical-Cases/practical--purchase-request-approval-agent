# Reset only the educational cache between isolated test cases.
import pytest
from app.providers.dependencies import get_purchase_store

@pytest.fixture(autouse=True)
def reset_store():
    get_purchase_store.cache_clear()
    yield
    get_purchase_store.cache_clear()
