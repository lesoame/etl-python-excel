from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class SalesSheet(BaseModel):
    Organizador: int = Field(..., description="Identificador do organizador")
    Ano_Mes: str = Field(..., description="Ano e mês do registro")
    Dia_da_Semana: str = Field(..., description="Dia da semana correspondente à data")
    Tipo_Dia: str = Field(..., description="Classificação do dia: útil, fim de semana ou feriado")
    Objetivo: str = Field(..., description="Objetivo da campanha ou ação")
    Date: date = Field(..., description="Data da entrada no formato YYYY-MM-DD")
    AdSet_name: str = Field(..., description="Nome do conjunto de anúncios")
    Amount_spent: float = Field(0.0, ge=0, le=1200, description="Valor gasto no anúncio (mínimo 0, máximp 1200)")
    Link_clicks: Optional[float] = Field(None, description="Número de cliques no link")
    Impressions: int = Field(..., description="Número de impressões do anúncio")
    Conversions: Optional[float] = Field(None, description="Número de conversões registradas")
    Segmentacao: Optional[str] = Field(None, description="Segmentação usada no anúncio")
    Tipo_de_Anuncio: Optional[str] = Field(None, description="Tipo de anúncio")
    Fase: Optional[str] = Field(None, description="Fase da campanha")

    class Config:
        extra = "ignore"  # Ignora campos extras no CSV