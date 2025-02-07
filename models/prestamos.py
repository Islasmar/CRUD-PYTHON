from models.materialBase import EstadoPrestamo
from sqlalchemy import Column, Integer, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base
import enum


# Modelo para Préstamos
class Prestamo(Base):
    __tablename__ = "tbb_prestamos"
    
    id_prestamo = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey("tbb_usuarios.id"), nullable=False)
    id_material = Column(Integer, ForeignKey("tbb_materiales.id_material"), nullable=False)
    fecha_prestamo = Column(DateTime, nullable=False)
    fecha_devolucion = Column(DateTime, nullable=True)
    estado_prestamo = Column(Enum(EstadoPrestamo), nullable=False)

    material = relationship("Material", back_populates="prestamos")