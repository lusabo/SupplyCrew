from fastapi import FastAPI
from app.routes import purchase_requests, catalog

app = FastAPI(title="SupplyCrew API")

app.include_router(purchase_requests.router)
app.include_router(catalog.router)
