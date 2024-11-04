# app/crud/crud.py
from sqlalchemy.orm import Session
from app.models.models import ReservasRecursos  # Cambia 'ModeloDeReserva' al nombre real de tu modelo SQLAlchemy
from app.schemas.schemas import ReservaRecursoSchema

def create_reserva_recurso(db: Session, reserva_recurso: ReservaRecursoSchema):
    db_item = ReservasRecursos(**reserva_recurso.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item