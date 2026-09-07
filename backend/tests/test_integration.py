import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_registrar_y_consultar_producto():
    """
    Prueba de integración (IT-01):
    Registrar un producto y verificar que se guarde correctamente en la base de datos.
    """
    # 1. Registrar producto
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

    # 2. Consultar producto por ID
    response = client.get(f"/productos/{producto_id}")
    assert response.status_code == 200
    assert response.json()["nombre"] == "Galaxy S24"
    assert response.json()["marca"] == "Samsung"
    assert response.json()["stock"] == 15

    # 3. Verificar que el producto aparece en la lista general
    response = client.get("/productos/")
    assert response.status_code == 200
    productos = response.json()
    assert any(p["id"] == producto_id for p in productos)