from fastapi import APIRouter, Depends, HTTPException, Response, status
from pydantic import BaseModel, ConfigDict, Field, field_validator
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_db
from models.categoria import Categoria


router = APIRouter(prefix="/categoria", tags=["Categoria"]
)
class CategoriaEntrada(BaseModel):
    nome: str = Field(min_length=1, max_length=150)
    cor_pin: str = Field(min_length=1, max_length=20)
    quorum_minimo: int
    nivel_urgengia: str = Field(min_length=1, max_length=20)

    @field_validator("nome")
    @classmethod
    def validar_nome(cls, valor: str) -> str:
        valor = valor.strip()

        if not valor:
            raise ValueError("O nome não pode ficar vazio.")

        return valor

class CateroriaSaida(CategoriaEntrada):
    model_config = ConfigDict(from_attributes=True)
    id_categoria: int

def buscar_categoria(id_categoria: int, db: Session) -> Categoria:
    categoria = db.get(Categoria, id_categoria)

    if categoria is None:
        raise HTTPException(
            status_code=404,
            detail="Categoria não encontrado."      
        )                    
    return categoria

@router.post(
    "",
    response_model=CateroriaSaida,
    status_code=status.HTTP_201_CREATED
)
def cadastrar_categoria(
    dados: CategoriaEntrada,
    db: Session = Depends(get_db)
):
    categoria = Categoria(**dados.model_dump())
    db.add(categoria)
    db.commit()
    db.refresh(categoria)
    return categoria

@router.get("", response_model=list[CateroriaSaida])
def listar_categorias(db: Session = Depends(get_db)):
    consulta = select(Categoria).order_by(Categoria.id_categoria)
    return db.scalars(consulta).all()

@router.get("/{id_categoria}", response_model=CateroriaSaida)
def consultar_categoria(
    id_categoria: int,
    db: Session = Depends(get_db)
):
    return buscar_categoria(id_categoria, db)

@router.put("/{id_categoria}", response_model=CateroriaSaida)
def atualizar_categoria(
    id_categoria: int,
    dados: CategoriaEntrada,
    db: Session = Depends(get_db)
):
    categoria = buscar_categoria(id_categoria, db)
    categoria.nome = dados.nome
    categoria.cor_pin = dados.cor_pin
    categoria.quorum_minimo = dados.quorum_minimo
    categoria.nivel_urgengia = dados.nivel_urgengia
    db.commit()
    db.refresh(categoria)
    return categoria

@router.delete(
    "/{id_categoria}",
    status_code=status.HTTP_204_NO_CONTENT
)
def excluir_categoria(
    id_categoria: int,
    db: Session = Depends(get_db)
):
    categoria = buscar_categoria(id_categoria, db)
    db.delete(categoria)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)