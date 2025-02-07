from fastapi import FastAPI
from routes.users import user
from routes.materialBase import material
from routes.prestamos import prestamo

app = FastAPI(
    title="Prestamos S.A de C.V",
    description="Api de prueba para almacenar registros de prestamos de material educativo")

app.include_router(user)
app.include_router(material)
app.include_router(prestamo)