from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import SessionLocal
from schemas.recursos_reservas_schemas import RecursoReservaCreate, RecursoReserva
from crud.recurso_reserva_crud import create_recurso_reserva



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