from pydantic import BaseModel



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

class RecursoReserva(RecursoReservaCreate):
    id: int
    
    
    class Config:
        orm_mode = True