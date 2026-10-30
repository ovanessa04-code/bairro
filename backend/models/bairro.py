from sqlalchemy import Identity, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from database import Base 

class Bairro(Base):
    __tablebairro__= "bairro"
    __table_args__={"schema": "public"}

    id_bairro: Mapped[int] = mapped_column(
        Integer,
        Identity(always=True),
        primary_key=True, 
    )
    nome_bairro: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )
    cidade: Mapped[str] = mapped_column(
        String(100),
        nullable=False,

    )   
    estado: Mapped[Optional[str]] = mapped_column(
        String(2),
        nullable=True,
    )


    
