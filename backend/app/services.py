from typing import List, Optional
from .models import Producto

productos_db = []
contador_id = 1

def registrar_producto(producto: Producto) -> Producto:
    global contador_id
    producto.id = contador_id
    contador_id += 1
    productos_db.append(producto)
    return producto

def obtener_productos() -> List[Producto]:
    return productos_db

def obtener_producto_por_id(producto_id: int) -> Optional[Producto]:
    for p in productos_db:
        if p.id == producto_id:
            return p
    return None

def actualizar_producto(producto_id: int, datos: Producto) -> Optional[Producto]:
    for i, p in enumerate(productos_db):
        if p.id == producto_id:
            datos.id = producto_id
            productos_db[i] = datos
            return datos
    return None

def eliminar_producto(producto_id: int) -> bool:
    for i, p in enumerate(productos_db):
        if p.id == producto_id:
            productos_db.pop(i)
            return True
    return False

def buscar_productos(termino: str) -> List[Producto]:
    resultados = []
    for p in productos_db:
        if (termino.lower() in p.nombre.lower() or
            termino.lower() in p.marca.lower() or
            termino.lower() in p.modelo.lower() or
            termino in p.imei):
            resultados.append(p)
    return resultados

def verificar_stock_bajo(producto: Producto) -> bool:
    return producto.stock <= producto.umbral_alerta

def calcular_precio_venta(precio_compra: float, margen: float = 0.30) -> float:
    return round(precio_compra * (1 + margen), 2)

def actualizar_stock(producto_id: int, cantidad: int) -> Optional[Producto]:
    producto = obtener_producto_por_id(producto_id)
    if producto and producto.stock >= cantidad:
        producto.stock -= cantidad
        return producto
    return None