from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.materialBase
import config.db
import schemas.materialBase
import models.materialBase
from typing import List

material = APIRouter()

models.materialBase.Base.metadata.create_all(bind=config.db.engine)

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()
#Se obtienen los datos de manera general 
@material.get("/material/", response_model=List[schemas.materialBase.Material], tags=["Materiales"])
async def read_materiales(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_materiales = crud.materialBase.get_materiales(db=db, skip=skip, limit=limit)
    return db_materiales

# Obtener un material por ID
@material.get("/material/{id}", response_model=schemas.materialBase.Material, tags=["Materiales"])
async def read_material(id: int, db: Session = Depends(get_db)):
    db_material = crud.materialBase.get_material(db=db, id=id)
    if db_material is None:
        raise HTTPException(status_code=404, detail="El materal no existe")
    return db_material

# Crear un nuevo material
@material.post("/material/", response_model=schemas.materialBase.Material, tags=["Materiales"])
async def create_material(material: schemas.materialBase.MaterialCreate, db: Session = Depends(get_db)):
    return crud.materialBase.create_material(db=db, material=material)

# Actualizar un material existente en la base de datos

@material.put("/material/{id}", response_model=schemas.materialBase.Material, tags=["Materiales"])
async def update_material(id: int, material: schemas.materialBase.MaterialUpdate, db: Session = Depends(get_db)):
    db_material = crud.materialBase.get_material(db=db, id=id, material=material)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material no encontrado")
    return db_material

# Eliminar un material existente en la base de datos

@material.delete("/material/{id}", response_model=schemas.materialBase.Material, tags=["Materiales"])
async def delete_material(id: int, db: Session = Depends(get_db)):
    db_material = crud.materialBase.get_material(db=db, id=id)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material no encontrado")
    return db_material