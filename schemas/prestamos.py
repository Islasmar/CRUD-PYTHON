from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

# Modelo base para Préstamos
class PrestamoBase(BaseModel):
    id_usuario: int  # Clave foránea
    id_material: int  # Clave foránea
    fecha_prestamo: datetime
    fecha_devolucion: Optional[datetime]
    estado_prestamo: str  # Activo, Devuelto, Vencido

class PrestamoCreate(PrestamoBase):
    pass

class PrestamoUpdate(PrestamoBase):
    pass

class Prestamo(PrestamoBase):
    id_prestamo: int
    class Config:
        orm_mode = True