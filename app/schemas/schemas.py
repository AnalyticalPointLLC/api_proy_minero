from pydantic import BaseModel
from typing import Optional

class ReservaRecursoSchema(BaseModel):
    operacion_id: int
    tipo: str
    anio: int
    tonnes: float
    zn_kt: float
    pb_kt: float
    cu_kt: Optional[float] = None  # Asumiendo que estos campos pueden ser opcionales
    au_koz: Optional[float] = None
    ag_koz: Optional[float] = None
    zn_usdt: float  # Asegurarse de que los nombres coincidan con los del modelo
    pb_usdt: float
    cu_usdt: Optional[float] = None
    au_usdoz: Optional[float] = None
    ag_usdoz: Optional[float] = None
    zn_recovery: float
    pb_recovery: float
    cu_recovery: Optional[float] = None
    au_recovery: Optional[float] = None
    ag_recovery: Optional[float] = None

    class Config:
        orm_mode = True