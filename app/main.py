# ASGI assembly: HTTP doors have no procurement decisions inside them.
from fastapi import FastAPI
from app.features.purchase_requests.door import router as purchase_router
from app.features.approval.door import router as approval_router
app=FastAPI(title="Northstar Purchase Request Approval Agent")
app.include_router(purchase_router)
app.include_router(approval_router)
