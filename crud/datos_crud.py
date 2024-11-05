
from sqlalchemy.orm import Session
from db.models import YearData, TypeColumn, PhaseEstimation



def get_year_data(db: Session, skip: int = 0, limit: int = 100):
    return db.query(YearData).offset(skip).limit(limit).all()

def get_type_column(db: Session, skip: int = 0, limit: int = 100):
    return db.query(TypeColumn).offset(skip).limit(limit).all()

def get_phase_estimation(db: Session, skip: int = 0, limit: int = 100):
    return db.query(PhaseEstimation).offset(skip).limit(limit).all()