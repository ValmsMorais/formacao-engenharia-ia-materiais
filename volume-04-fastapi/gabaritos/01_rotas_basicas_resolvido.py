from fastapi import FastAPI

app = FastAPI()

@app.get("/status")
def status():
    return {"status": "ok"}

@app.get("/clientes/{cliente_id}")
def cliente(cliente_id: int):
    return {"id": cliente_id}

@app.get("/transacoes")
def transacoes(tipo: str | None = None, limite: int = 20):
    return {"tipo": tipo, "limite": limite}
