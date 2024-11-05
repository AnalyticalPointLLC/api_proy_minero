from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import Datos
from schemas import DatosCreate

async def create_datos(db: AsyncSession, datos: DatosCreate):
    db_datos = Datos(**datos.dict())
    db.add(db_datos)
    await db.commit()
    await db.refresh(db_datos)
    return db_datos