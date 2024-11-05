from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import SessionLocal
from schemas.recursos_reservas_schemas import RecursoReservaCreate, RecursoReserva, RecursoReservaCompleto
from crud.recurso_reserva_crud import create_recurso_reserva, get_recursos_reservas_completos


app = FastAPI()

# Dependencia
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/recursos-reservas-completo/", response_model=List[RecursoReserva])
def read_recursos_reservas_completo(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # Aquí asumimos que tienes una función en un CRUD o similar para obtener los datos combinados.
    datos_completos = get_recursos_reservas_completos(db, skip=skip, limit=limit)
    return datos_completos