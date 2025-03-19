from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración de la base de datos
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://avnadmin:AVNS_AZ-uFpCyNqT_2gDRgYA@mysql-prestamos-prestamosutxj2.c.aivencloud.com:24041/baseprueba"

# Crear el motor (engine)
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# Crear la sesión
SesionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Definir el objeto base para los modelos
Base = declarative_base()

from models.materiales import Material
from models.prestamos import Prestamo
import models.user as User

# Crear las tablas en orden específico
#Material.__table__.create(bind=engine)
