from fastapi import FastAPI, HTTPException, Body
from database import engine, Base
from routes import datos_route


app = FastAPI()

# Crear las tablas en la base de datos, si aún no existen
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.on_event("startup")
async def startup_event():
    await create_tables()

app.include_router(datos_route.router)








# main.py
from fastapi import FastAPI
from .datos_route import router as datos_router  # Ajusta la importación según tu estructura

app = FastAPI()

app.include_router(datos_router)