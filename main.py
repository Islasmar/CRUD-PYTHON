from fastapi import FastAPI
from routes.userRoutes import user
from routes.prestamos import prestamo
from routes.materiales import material
from fastapi.middleware.cors import CORSMiddleware
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.on_event("startup")
async def startup_event():
    routes = [route.path for route in app.router.routes]
    logger.info(f"📌 Rutas registradas: {routes}")



app = FastAPI(
    title="Example S.A de C.V",
    description="API de prueba para almacenar usuarios"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user)
app.include_router(prestamo)
app.include_router(material)
