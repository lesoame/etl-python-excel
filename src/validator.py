from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class User(BaseModel):
    Organizador: int
    Ano_Mes: str
    Dia_da_Semana: str
    Tipo_Dia: str
    Objetivo: str
    Date: date
    AdSet_name: str
    Amount_spent: float = Field(ge=0)  # Ensuring non-negative values
    Link_clicks: Optional[int]
    Impressions: int
    Conversions: Optional[int]
    Segmentacao: str
    Tipo_de_Anuncio: str
    Fase: str

user = User()
print(user)
#> name='John Doe'