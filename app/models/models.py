from sqlalchemy import Column, Integer, Numeric, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.database import Base

class ReservasRecursos(Base):
    __tablename__ = "reservasrecursos"
    
    id = Column(Integer, primary_key=True, index=True)
    operacion_id = Column(Integer, ForeignKey('operacion.id'), nullable=False)
    tipo = Column(String)
    anio = Column(Integer)
    tonnes = Column(Numeric(18,2))
    zn_kt = Column(Numeric(18,2))
    pb_kt = Column(Numeric(18,2))
    cu_kt = Column(Numeric(18,2))
    au_koz = Column(Numeric(18,2))
    ag_koz = Column(Numeric(18,2))
    zn_usdt = Column(Numeric(18,2))
    pb_usdt = Column(Numeric(18,2))
    cu_usdt = Column(Numeric(18,2))
    au_usdoz = Column(Numeric(18,2))
    ag_usdoz = Column(Numeric(18,2))
    zn_recovery = Column(Numeric(18,2))
    pb_recovery = Column(Numeric(18,2))
    cu_recovery = Column(Numeric(18,2))
    au_recovery = Column(Numeric(18,2))
    ag_recovery = Column(Numeric(18,2))
    
    
    
    # Añade el resto de tus columnas aquí...