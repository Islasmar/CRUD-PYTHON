from sqlalchemy.orm import Session
from models.prestamos import Prestamo, EstadoPrestamo
from schemas.prestamos import PrestamoCreate, PrestamoUpdate

def get_prestamo(db: Session, id: int):
    return db.query(Prestamo).filter(Prestamo.id_prestamo == id).first()

def get_prestamos(db: Session, skip: int = 0, limit: int = 0):
    return db.query(Prestamo).offset(skip).limit(limit).all()

def create_prestamo(db: Session, prestamo: PrestamoCreate):
    db_prestamo = Prestamo(
        id_material=prestamo.id_material,
        id_usuario=prestamo.id_usuario,
        fecha_prestamo=prestamo.fecha_prestamo,
        fecha_devolucion=prestamo.fecha_devolucion,
        estado_prestamo=prestamo.estado_prestamo
    )
    db.add(db_prestamo)
    db.commit()
    db.refresh(db_prestamo)
    return db_prestamo

def update_prestamo(db: Session, id: int, prestamo: PrestamoUpdate):
    db_prestamo = db.query(Prestamo).filter(Prestamo.id_prestamo == id).first()
    if db_prestamo:
        for var, value in vars(prestamo).items():
            setattr(db_prestamo, var, value) if value else None
        db.commit()
        db.refresh(db_prestamo)
    return db_prestamo

def delete_prestamo(db: Session, id: int):
    db_prestamo = db.query(Prestamo).filter(Prestamo.id_prestamo == id).first()
    if db_prestamo:
        db.delete(db_prestamo)
        db.commit()
    return db_prestamo