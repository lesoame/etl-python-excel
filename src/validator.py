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
    Amount_spent: float = Field(0.0, ge=0, le=1200, description="Valor gasto no anúncio (mínimo 0, máximp 1200)")  # Ensuring non-negative values
    Link_clicks: Optional[int] = Field(None, description="Número de cliques no link")
    Impressions: int = Field(..., description="Número de impressões do anúncio")
    Conversions: Optional[int] = Field(None, description="Número de conversões registradas")
    Segmentacao: str = Field(..., description="Segmentação usada no anúncio")
    Tipo_de_Anuncio: str = Field(..., description="Tipo de anúncio")
    Fase: str = Field(..., description="Fase da campanha")
