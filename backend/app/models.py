from pydantic import BaseModel
from typing import Optional

class Producto(BaseModel):
    id: Optional[int] = None
    nombre: str
    marca: str
    modelo: str
    imei: str
    precio_compra: float
    precio_venta: float
    stock: int
    umbral_alerta: int = 5