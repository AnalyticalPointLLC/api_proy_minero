from sqlalchemy import Column, Integer, Numeric, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class RecursoReserva(Base):
    __tablename__ = "recursos_reservas"
    id = Column(Integer, primary_key=True, index=True)
    operation_id = Column(Integer, index=True)
    type_column = Column(String, index=True)
    year_data = Column(Integer, index=True)
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
    phase_estimation = Column(String, nullable=False)
    comments_detail = Column(String, nullable=False)
    meta1 = Column(Numeric(18,2))
    meta2 = Column(Numeric(18,2))
    
class YearData(Base):
    __tablename__ = "year_data"
    id = Column(Integer, primary_key=True, index=True)
    year_data = Column(Integer, unique=True, nullable=False)
    
class TypeColumn(Base):
    __tablename__ = "type_column"
    id = Column(Integer, primary_key=True, index=True)
    type_column = Column(String, unique=True, nullable=False)
    
class PhaseEstimation(Base):
    __tablename__ = "phase_estimation"
    id = Column(Integer, primary_key=True, index=True)
    phase_estimation = Column(String, unique=True, nullable=False)
 