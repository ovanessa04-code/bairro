from fastapi import APIRouter, Depends, HTTPException, Response, status
from pydantic import BaseModel, ConfigDict, Field, field_validator
from sqlalchemy import select
from sqlalchemy.orm import Session
from database import get_db
from models.bairro import Bairro 

router = APIRouter(prefix="/bairros", tags=["Bairros"])

class BairroEntrada(BaseModel):
    nome_bairro: str = Field(min_length=1, max_length=150)
    cidade: str = Field(min_length=1, max_length=100)
    estado: str = Field(min_length=1, max_length=2)


@field_validator("nome_bairro")
@classmethod
def validar_nome(cls, valor: str) -> str:
    valor = valor.strip()
    if not valor:
        raise ValueError("O nome não pode ficar vazio.")
    return valor

class BairroSaida(BairroEntrada):
    model_config = ConfigDict(from_attributes=True)
    id_bairro: int

def buscar_bairro(id_bairro: int, db: Session) -> Bairro:
    bairro = db.get(Bairro, id_bairro)
    if bairro is None:
        raise HTTPException(
    status_code=404,
    detail="Bairro não encontrado.",
    )
    return bairro

@router.post("", response_model=BairroSaida,
    status_code=status.HTTP_201_CREATED)
def cadastrar_bairro(dados: BairroEntrada,
        db: Session = Depends(get_db)):
    bairro = Bairro(**dados.model_dump())
    db.add(bairro)
    db.commit()
    db.refresh(bairro)
    return bairro

@router.get("", response_model=list[BairroSaida])
def listar_bairro(db: Session = Depends(get_db)):
    consulta = select(Bairro).order_by(Bairro.id_bairro)
    return db.scalars(consulta).all()

@router.get("/{id_bairro}", response_model=BairroSaida)
def consultar_bairro(id_bairro: int,
                db: Session = Depends(get_db)):
    return buscar_bairro(id_bairro, db )

@router.put("/{id_bairro}", response_model=BairroSaida)
def atualizar_bairro(id_bairro: int, dados: BairroEntrada,
        db: Session = Depends(get_db)):
    bairro = buscar_bairro(id_bairro , db)
    bairro.nome_bairro = dados.nome_bairro
    bairro.cidade = dados.cidade
    bairro.estado = dados.estado
    db.commit()
    db.refresh(bairro)
    return bairro

@router.delete("/{id_bairro}",
    status_code=status.HTTP_204_NO_CONTENT)
def excluir_bairro(id_bairro: int,
        db: Session = Depends(get_db)):
    bairro = buscar_bairro(id_bairro, db)
    db.delete(bairro)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)