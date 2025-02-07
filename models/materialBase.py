from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from config.db import Base
import enum

# Enumeraciones para los estados
class EstadoMaterial(str, enum.Enum):
    Disponible = "Disponible"
    Prestado = "Prestado"
    EnMantenimiento = "En Mantenimiento"

class EstadoPrestamo(str, enum.Enum):
    Activo = "Activo"
    Devuelto = "Devuelto"
    Vencido = "Vencido"

# Modelo para Materiales
class Material(Base):
    __tablename__ = "tbb_materiales"
    
    id_material = Column(Integer, primary_key=True, autoincrement=True)
    tipo_material = Column(String(100), nullable=False)
    marca = Column(String(100), nullable=False)
    modelo = Column(String(100), nullable=False)
    estado = Column(Enum(EstadoMaterial), nullable=False)

    prestamos = relationship("Prestamo", back_populates="material")