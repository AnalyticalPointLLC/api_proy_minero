from fastapi import FastAPI, HTTPException, Body

from routers.recursos_reservas_router import router as recurso_reserva_router
from routers.datos_router import router as year_data_router




app = FastAPI()


app.include_router(recurso_reserva_router, prefix="/recursos_reservas", tags=["recursos_reservas"])
app.include_router(year_data_router)






