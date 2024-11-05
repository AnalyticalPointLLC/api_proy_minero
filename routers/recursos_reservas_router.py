from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from db.database import SessionLocal
from schemas.recursos_reservas_schemas import RecursoReservaCreate, RecursoReserva, RecursoReservaCompleto
from crud.recurso_reserva_crud import create_recurso_reserva, get_recursos_reservas_completos



router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=RecursoReserva)
def create_recurso_reserva_endpoint(recurso_reserva: RecursoReservaCreate, db: Session = Depends(get_db)):
    return create_recurso_reserva(db=db, recurso_reserva=recurso_reserva)



@router.get("/completos/{operation_id}/{type_column}/{year_data}", response_model=List[RecursoReservaCompleto])
def read_recursos_reservas_completos(operation_id: int, type_column: str, year_data: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        recursos_reservas_completos = get_recursos_reservas_completos(db, operation_id, type_column, year_data, skip=skip, limit=limit)
        return recursos_reservas_completos
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))