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
    