from pydantic import BaseModel



class YearDataBase(BaseModel):
    id: int
    year_data: int

class YearDataList(YearDataBase):
    id: int
   




class TypeColumnBase(BaseModel):
    id: int
    type_column: str

class TypeColumnList(TypeColumnBase):
    id: int




    
class PhaseEstimationBase(BaseModel):
    id: int
    phase_estimation: str
    
class PhaseEstimationList(PhaseEstimationBase):
    id: int

    
    class Config:
        orm_mode = True