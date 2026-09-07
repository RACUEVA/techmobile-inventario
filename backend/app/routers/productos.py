from fastapi import APIRouter, HTTPException, Query
from typing import List

# Importar los modelos y servicios
from app.models import Producto
from app.services import (
    registrar_producto,
    obtener_productos,
    obtener_producto_por_id,
    actualizar_producto,
    eliminar_producto,
    buscar_productos,
    actualizar_stock
)

# ⭐ CREAR EL ROUTER 
router = APIRouter(prefix="/productos", tags=["Productos"])

@router.post("/", response_model=Producto)
def crear_producto(producto: Producto):
    return registrar_producto(producto)

@router.get("/", response_model=List[Producto])
def listar_productos():
    return obtener_productos()

@router.get("/{producto_id}", response_model=Producto)
def obtener_producto(producto_id: int):
    producto = obtener_producto_por_id(producto_id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@router.put("/{producto_id}", response_model=Producto)
def modificar_producto(producto_id: int, datos: Producto):
    resultado = actualizar_producto(producto_id, datos)
    if not resultado:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return resultado

@router.delete("/{producto_id}")
def eliminar_producto_endpoint(producto_id: int):
    if not eliminar_producto(producto_id):
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"mensaje": "Producto eliminado correctamente"}

@router.get("/buscar/", response_model=List[Producto])
def buscar_productos_endpoint(q: str = Query(..., min_length=1)):
    return buscar_productos(q)

@router.post("/{producto_id}/vender")
def vender_producto(producto_id: int, cantidad: int = Query(..., gt=0)):
    producto = actualizar_stock(producto_id, cantidad)
    if not producto:
        raise HTTPException(status_code=400, detail="Stock insuficiente o producto no encontrado")
    return {"mensaje": "Venta registrada", "stock_restante": producto.stock}