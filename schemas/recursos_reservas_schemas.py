from pydantic import BaseModel
from typing import Optional



class RecursoReservaCreate(BaseModel):
    operation_id: int
    type_column: str
    year_data: int
    tonnes: float
    zn_kt: float
    pb_kt: float
    cu_kt: float
    au_koz: float
    ag_koz: float
    zn_usdt: float
    pb_usdt: float
    cu_usdt: float
    au_usdoz: float
    ag_usdoz: float
    zn_recovery: float
    pb_recovery: float
    cu_recovery: float
    au_recovery: float
    ag_recovery: float
    phase_estimation: str
    comments_detail: str
    meta1: float
    meta2: float
    
    class Config:
        orm_mode = True

class RecursoReserva(RecursoReservaCreate):
    id: int


class RecursoReservaPercentCreate(BaseModel):
    recursos_reservas_id: int
    zn_kt: float
    pb_kt: float
    cu_kt: float
    au_koz: float
    ag_koz: float
    
class RecursoReservaPercent(RecursoReservaPercentCreate):
    id: int
    
    class Config:
        orm_mode = True
        
        
        
#COMPLETO SALIDA FINAL
class RecursoReservaCompleto(BaseModel):
    operation_id: int
    type_column: str
    year_data: int
    tonnes: Optional[float] = None
    zn_percent: Optional[float] = None
    pb_percent: Optional[float] = None
    cu_percent: Optional[float] = None
    au_gt: Optional[float] = None
    ag_gt: Optional[float] = None
    zn_kt: float
    pb_kt: float
    cu_kt: float
    au_koz: float
    ag_koz: float
    zn_usdt: float
    pb_usdt: float
    cu_usdt: float
    au_usdoz: float
    ag_usdoz: float
    zn_recovery: float
    pb_recovery: float
    cu_recovery: float
    au_recovery: float
    ag_recovery: float
    phase_estimation: str
    comments_detail: str
    meta1: float
    meta2: float
    
    class Config:
        orm_mode = True