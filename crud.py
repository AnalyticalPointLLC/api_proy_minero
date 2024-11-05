from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from sqlalchemy.future import select
from models import Datos
from schemas import DatosCreate

from . import models

async def create_datos(db: AsyncSession, datos: DatosCreate):
    db_datos = Datos(**datos.dict())
    db.add(db_datos)
    await db.commit()
    await db.refresh(db_datos)
    return db_datos


def get_year_data(db: Session):
    return db.query(models.YearData).all()

def get_type_column(db: Session):
    return db.query(models.TypeColumn).all()

def get_phase_estimation(db: Session):
    return db.query(models.PhaseEstimation).all()