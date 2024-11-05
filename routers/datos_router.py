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