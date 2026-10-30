from fastapi import APIRouter, Depends, HTTPException, Response, status
from pydantic import BaseModel, ConfigDict, Field, field_validator
from sqlalchemy import select
from sqlalchemy.orm import Session
from database import get_db
from models.bairro import Bairro 

router = APIRouter(prefix="/bairro", tags=["bairro"])

class BairroEntrada(BaseModel):
    