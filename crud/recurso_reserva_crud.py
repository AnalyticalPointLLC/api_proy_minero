
from sqlalchemy.orm import Session
from db.models import RecursoReserva, RecursoReservaPercent
from decimal import Decimal





def create_recurso_reserva(db: Session, recurso_reserva: RecursoReserva):
    db_recurso_reserva = RecursoReserva(**recurso_reserva.dict())
    db.add(db_recurso_reserva)
    db.commit()
    db.refresh(db_recurso_reserva)
    
    # Asegúrate de que tonnes no sea cero para evitar la división por cero
    if db_recurso_reserva.tonnes != 0:
        tonnes_decimal = Decimal(db_recurso_reserva.tonnes)
    
    # Aquí calculas los porcentajes y gt para RecursoReservaPercent
    # Esto es un ejemplo genérico. Debes adaptar los cálculos a tus necesidades específicas.
    zn_percent = (Decimal(db_recurso_reserva.zn_kt) / tonnes_decimal) / Decimal('10')
    pb_percent = (Decimal(db_recurso_reserva.pb_kt) / tonnes_decimal) / Decimal('10')
    cu_percent = (Decimal(db_recurso_reserva.cu_kt) / tonnes_decimal) / Decimal('10')
    au_gt = (Decimal(db_recurso_reserva.au_koz) / tonnes_decimal) * Decimal('31.1035') / Decimal('1000') # Convertir onzas a gramos y dividir por toneladas
    ag_gt = (Decimal(db_recurso_reserva.ag_koz) / tonnes_decimal) * Decimal('31.1035') / Decimal('1000') # Convertir onzas a gramos y dividir por toneladas
    
    # Crear y añadir el nuevo RecursoReservaPercent asociado
    db_recurso_reserva_percent = RecursoReservaPercent(
        recursos_reservas_id=db_recurso_reserva.id,
        zn_percent=zn_percent,
        pb_percent=pb_percent,
        cu_percent=cu_percent,
        au_gt=au_gt,
        ag_gt=ag_gt
    )
    db.add(db_recurso_reserva_percent)
    db.commit()
    db.refresh(db_recurso_reserva_percent)
    
    
    return db_recurso_reserva



def get_recursos_reservas_completos(db: Session, type_column: str, year_data: int, skip: int = 0, limit: int = 100):
    return db.query(
        RecursoReserva.tonnes,
        RecursoReservaPercent.zn_percent,
        RecursoReservaPercent.pb_percent,
        RecursoReservaPercent.cu_percent,
        RecursoReservaPercent.au_gt,
        RecursoReservaPercent.ag_gt,
        RecursoReserva.zn_kt,
        RecursoReserva.pb_kt,
        RecursoReserva.cu_kt,
        RecursoReserva.au_koz,
        RecursoReserva.ag_koz,
        RecursoReserva.zn_usdt,
        RecursoReserva.pb_usdt,
        RecursoReserva.cu_usdt,
        RecursoReserva.au_usdoz,
        RecursoReserva.ag_usdoz,
        RecursoReserva.zn_recovery,
        RecursoReserva.pb_recovery,
        RecursoReserva.cu_recovery,
        RecursoReserva.au_recovery,
        RecursoReserva.ag_recovery,
        RecursoReserva.phase_estimation,
        RecursoReserva.comments_detail,
        RecursoReserva.meta1,
        RecursoReserva.meta2
    ).join(RecursoReservaPercent, RecursoReserva.id == RecursoReservaPercent.recursos_reservas_id)\
    .filter(RecursoReserva.type_column == type_column)\
    .filter(RecursoReserva.year_data == year_data)\
    .offset(skip)\
    .limit(limit)\
    .all()