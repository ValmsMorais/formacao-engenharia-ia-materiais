from pydantic import BaseModel

class ClienteCriacao(BaseModel):
    nome: str
    documento: str

class ClienteAtualizacao(BaseModel):
    nome: str | None = None
    ativo: bool | None = None

class ClienteSaida(BaseModel):
    id: int
    nome: str
    documento: str
    ativo: bool
