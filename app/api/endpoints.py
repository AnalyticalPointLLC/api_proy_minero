from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.crud.crud import create_reserva_recurso  # Asumiendo que esta función existe en tu módulo crud
from app.schemas import ReservaRecursoSchema  # Importación actualizada basada en schemas.py
from app.database.database import SessionLocal  # Importación correcta, asumiendo que este es el path

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/reservas-recursos/", response_model=ReservaRecursoSchema)
def create_reserva_recurso_endpoint(reserva_recurso: ReservaRecursoSchema, db: Session = Depends(get_db)):
    print(reserva_recurso)  # Solo para depuración, considera usar logging en producción

    try:
        db_reserva_recurso = create_reserva_recurso(db=db, reserva_recurso=reserva_recurso)
        return db_reserva_recurso
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))