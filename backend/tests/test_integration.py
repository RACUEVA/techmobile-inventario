import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_registrar_y_consultar_producto():
    # Registrar producto
    response = client.post("/productos/", json={
        "nombre": "Galaxy S24",
        "marca": "Samsung",
        "modelo": "SM-S921B",
        "imei": "987654321098765",
        "precio_compra": 700.0,
        "precio_venta": 1000.0,
        "stock": 15
    })
    assert response.status_code == 200
    data = response.json()
    producto_id = data["id"]

    # Consultar producto
    response = client.get(f"/productos/{producto_id}")
    assert response.status_code == 200
    assert response.json()["nombre"] == "Galaxy S24"