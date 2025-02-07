from sqlalchemy.orm import Session
from models.materialBase import Material, EstadoMaterial
from schemas.materialBase import MaterialCreate, MaterialUpdate

def get_material(db: Session, id: int):
    return db.query(Material).filter(Material.id_material == id).first()
def get_materiales(db: Session, skip: int = 0, limit: int = 0):
    return db.query(Material).offset(skip).limit(limit).all()

def create_material(db: Session, material: MaterialCreate):
    db_material = Material(
        tipo_material=material.tipo_material,
        marca=material.marca,
        modelo=material.modelo,
        estado=material.estado
    )
    db.add(db_material)
    db.commit()
    db.refresh(db_material)
    return db_material

def update_material(db: Session, id: int, material: MaterialUpdate):
    db_material = db.query(Material).filter(Material.id_material == id).first()
    if db_material:
        for var, value in vars(material).items():
            setattr(db_material, var, value) if value else None
        db.commit()
        db.refresh(db_material)
        return db_material

def delete_material(db: Session, id: int):
    db_material = db.query(Material).filter(Material.id_material == id).first()
    if db_material:
        db.delete(db_material)
        db.commit()
    return db_material
