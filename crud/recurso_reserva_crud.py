
from sqlalchemy.orm import Session
from db.models import RecursoReserva




def create_recurso_reserva(db: Session, recurso_reserva: RecursoReserva):
    db_recurso_reserva = RecursoReserva(**recurso_reserva.dict())
    db.add(db_recurso_reserva)
    db.commit()
    db.refresh(db_recurso_reserva)
    return db_recurso_reserva

