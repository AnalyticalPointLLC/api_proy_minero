# Importaciones necesarias
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from database import SessionLocal
from schemas import DatosBase, YearDataSchema, TypeColumnSchema, PhaseEstimationSchema # Asegúrate de que este importe es correcto y refleja tu estructura
from models import YearData, TypeColumn, PhaseEstimation
import crud

router = APIRouter()

# Dependencia para obtener la sesión de la base de datos
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()

@router.post("/datos/")
async def create_datos(datos: DatosBase, db: AsyncSession = Depends(get_db)):
    created_data = await crud.create_datos(db=db, datos=datos)  # Asume que esta función maneja correctamente los datos

    # Prepare la respuesta considerando que phase_estimation podría ser None
    phase_estimation_value = datos.phase_estimation.value if datos.phase_estimation else None

    # Asume que created_data es una instancia del modelo de SQLAlchemy y tiene un atributo 'id'
    return {
        "message": "Datos recibidos correctamente",
        "id": created_data.id,  # Ejemplo de cómo podrías querer incluir el ID del objeto creado
        "phase_estimation": phase_estimation_value
    }
    
    

    
@router.get("/year_data/", response_model=list[YearDataSchema])
async def read_years(db: AsyncSession = Depends(get_db)):
    async with db as session:
        result = await session.execute(select(YearData))
        years_list = result.scalars().all()
        return years_list


    
@router.get("/type_column/", response_model=list[TypeColumnSchema])
async def read_years(db: AsyncSession = Depends(get_db)):
    async with db as session:
        result = await session.execute(select(TypeColumn))
        type_column = result.scalars().all()
        return type_column
    
    
@router.get("/phase_estimation/", response_model=list[PhaseEstimationSchema])
async def read_years(db: AsyncSession = Depends(get_db)):
    async with db as session:
        result = await session.execute(select(PhaseEstimation))
        phase_estimation = result.scalars().all()
        return phase_estimation
    
