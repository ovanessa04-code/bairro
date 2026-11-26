from fastapi import FastAPI
from controller.bairro import router as bairro_router
from controller.categoria import router as categoria_router
from pathlib import Path
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="Bairro - API do Bairro",
    description="CRUD do bairro com PostgreSQL local.",
)
app.include_router(bairro_router)
app.include_router(categoria_router) 

# Localiza a pasta frontend que fica ao lado do backend
PASTA_FRONTEND = Path(__file__).resolve().parent.parent/"frontend"

# Disponiliza as páginas, CSS, JavaScritp e imagens
app.mount("/", StaticFiles(directory=str(PASTA_FRONTEND),html=True),name="frontend")