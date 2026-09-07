from fastapi import FastAPI
from app.routers import productos

app = FastAPI(title="TechMobile Inventario API", version="1.0.0")

app.include_router(productos.router)

@app.get("/")
def root():
    return {"message": "API de inventario TechMobile funcionando"}

@app.get("/health")
def health():
    return {"status": "ok"}