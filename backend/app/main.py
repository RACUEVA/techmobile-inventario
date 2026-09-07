from fastapi import FastAPI

app = FastAPI(title="TechMobile Inventario API", version="1.0.0")

@app.get("/")
def root():
    return {"message": "API de inventario TechMobile funcionando"}

@app.get("/health")
def health():
    return {"status": "ok"}

# Configuración inicial del módulo de inventario