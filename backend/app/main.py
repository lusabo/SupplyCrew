from fastapi import FastAPI
from app.routes import purchase_requests

app = FastAPI(title="SupplyCrew API")

app.include_router(purchase_requests.router)
