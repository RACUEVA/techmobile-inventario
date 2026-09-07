from fastapi import FastAPI
import sys
import os

# Asegurar que el directorio actual esté en el path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.routers import productos

app = FastAPI(title="TechMobile Inventario API", version="1.0.0")

app.include_router(productos.router)

@app.get("/")
def root():
    return {"message": "API de inventario TechMobile funcionando"}

@app.get("/health")
def health():
    return {"status": "ok"}