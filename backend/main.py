from fastapi import FastAPI
from controller.bairro import router as bairro_router
from controller.categoria import router as categoria_router

app = FastAPI(
    title="Bairro - API do Bairro",
    description="CRUD do bairro com PostgreSQL local.",
)
app.include_router(bairro_router)
app.include_router(categoria_router) 
