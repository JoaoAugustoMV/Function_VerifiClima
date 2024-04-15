from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class InformacaoDiaTemperatura(Base):
    __tablename__ = "informacao_previsao_temperatura"
    id_dia: Mapped[int] = mapped_column(primary_key=True, autoincrement=False)
    x_dias: Mapped[int]

    dia_previsao_feita_menos_x: Mapped[datetime] = None
    temperatura_min_previsao_feita_menos_x: Mapped[int] = None
    temperatura_max_previsao_feita_menos_x: Mapped[int] = None
    
    temperatura_real_min: Mapped[int] = None
    temperatura_real_max: Mapped[int] = None
    
    fonte: Mapped[str]
    cidade: Mapped[str]
    descricao: Mapped[str] = ''