from fastapi import FastAPI

app = FastAPI()

@app.get("/clientes/{cliente_id}")
def cliente(cliente_id: int, detalhes: bool = False):
    return {"cliente_id": cliente_id, "detalhes": detalhes}
