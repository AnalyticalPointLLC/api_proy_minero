from pydantic import BaseModel, validator



class DatosBase(BaseModel):
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
    
    # @validator('phase_estimation', pre=True, always=True)
    # def check_fase_estimacion(cls, v):
    #     if v is None:
    #         raise ValueError("phase_estimation es un campo obligatorio")
    #     return v




class DatosCreate(DatosBase):
    pass

class Datos(DatosBase):
    id: int


class YearDataBase(BaseModel):
    id: int
    year_data: int

class YearDataList(BaseModel):
    id: int
   

class TypeColumnBase(BaseModel):
    id: int
    type_column: str

class TypeColumnList(BaseModel):
    id: int

    
class PhaseEstimationBase(BaseModel):
    id: int
    PhaseEstimation: str
    
class PhaseEstimationList(BaseModel):
    id: int

    
    class Config:
        orm_mode = True