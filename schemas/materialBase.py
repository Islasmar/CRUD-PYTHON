from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

# Modelo base para Materiales
class MaterialBase(BaseModel):
    tipo_material: str
    marca: str
    modelo: str
    estado: str

class MaterialCreate(MaterialBase):
    pass

class MaterialUpdate(MaterialBase):
    pass

class Material(MaterialBase):
    id_material: int
    class Config:
        orm_mode = True