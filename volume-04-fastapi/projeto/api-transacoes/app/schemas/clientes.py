from pydantic import BaseModel

class ClienteCriacao(BaseModel):
    nome: str
    documento: str

class ClienteSaida(BaseModel):
    id: int
    nome: str
    documento: str
    ativo: bool

    model_config = {"from_attributes": True}
