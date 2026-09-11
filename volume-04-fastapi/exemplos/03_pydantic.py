from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class TransacaoEntrada(BaseModel):
    cliente_id: int = Field(gt=0)
    valor: float = Field(gt=0)
    tipo: str = Field(pattern="^(CASHIN|CASHOUT)$")

@app.post("/transacoes", status_code=201)
def criar(dados: TransacaoEntrada):
    return dados
