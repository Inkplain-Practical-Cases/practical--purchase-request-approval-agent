# ASGI application entry point, no purchasing policy inside this door.
from fastapi import FastAPI
from app.features.purchase_requests.door import router
app = FastAPI(title="Northstar Purchase Request Approval Agent")
app.include_router(router)
