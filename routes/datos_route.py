# Importaciones necesarias
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from database import SessionLocal

from sqlalchemy.orm import Session
from .. import crud, models, schemas, database


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
    
    

    
@router.get("/year_data/", response_model=list[schemas.YearDataBase])
def read_year_data(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    year_data = crud.get_year_data(db=db, skip=skip, limit=limit)
    return year_data


    