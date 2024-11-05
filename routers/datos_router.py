from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import SessionLocal
from schemas.datos_schemas import YearDataBase, YearDataList, TypeColumnBase, TypeColumnList, PhaseEstimationBase, PhaseEstimationList
from crud.datos_crud import get_year_data, get_type_column, get_phase_estimation

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/year_data/", response_model=list[YearDataBase])
def read_year_data(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    year_data = get_year_data(db, skip=skip, limit=limit)
    return year_data

@router.get("/type_column/", response_model=list[TypeColumnBase])
def read_type_column(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    type_column = get_type_column(db, skip=skip, limit=limit)
    return type_column

@router.get("/phase_estimation/", response_model=list[PhaseEstimationBase])
def read_phase_estimation(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    phase_estimation = get_phase_estimation(db, skip=skip, limit=limit)
    return phase_estimation