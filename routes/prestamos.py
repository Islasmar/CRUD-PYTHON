from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.prestamos
import config.db
import schemas.prestamos
import models.prestamos
from typing import List

prestamo = APIRouter()

models.prestamos.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Obtener los prestamos en general
@prestamo.get("/prestamos/", response_model=List[schemas.prestamos.Prestamo], tags=["Préstamos"])
async def read_prestamos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_prestamos = crud.prestamos.get_prestamos(db=db, skip=skip, limit=limit)
    return db_prestamos

#Obtener un préstamo por ID
@prestamo.get("/prestamo/{id}", response_model=schemas.prestamos.Prestamo, tags=["Préstamos"])
async def read_prestamo(id: int, db: Session = Depends(get_db)):
    db_prestamo = crud.prestamos.get_prestamo(db=db, id=id)
    if db_prestamo is None:
        raise HTTPException(status_code=404, detail="Prestamo no encontrado")
    return db_prestamo

#Crear un nuevo préstamo
@prestamo.post("/prestamos/", response_model=schemas.prestamos.Prestamo, tags=["Préstamos"])
def create_prestamo(prestamo: schemas.prestamos.PrestamoCreate, db: Session = Depends(get_db)):
    return crud.prestamos.create_prestamo(db=db, prestamo=prestamo)

#Actualizar un préstamo existente
@prestamo.put("/prestamo/{id}", response_model=schemas.prestamos.Prestamo, tags=["Préstamos"])
def update_prestamo(id: int, prestamo: schemas.prestamos.PrestamoUpdate, db: Session = Depends(get_db)):
    db_prestamo = crud.prestamos.get_prestamo(db=db, id=id)
    if db_prestamo is None:
        raise HTTPException(status_code=404, detail="Prestamo no encontrado")
    return db_prestamo

#Eliminar un préstamo existente
@prestamo.delete("/prestamo/{id}", response_model=schemas.prestamos.Prestamo, tags=["Préstamos"])
def delete_prestamo(id: int, db: Session = Depends(get_db)):
    db_prestamo = crud.prestamos.get_prestamo(db=db, id=id)
    if db_prestamo is None:
        raise HTTPException(status_code=404, detail="Prestamo no encontrado")
    return db_prestamo