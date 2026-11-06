from sqlalchemy import Identity, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class Categoria(Base):
    __tablename__= "categoria" 
    __table_args__={"schema":"public"}

    id_categoria: Mapped[int] = mapped_column(
        Integer,
        Identity(always=True),
        primary_key=True,
    )
    nome: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )
    cor_pin: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )
    quorum_minimo: Mapped[int] = mapped_column(
        Integer,
        nullable= False
    )