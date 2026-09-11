import httpx

BASE_URL = "http://127.0.0.1:8000/api/v1"

with httpx.Client(base_url=BASE_URL, timeout=5.0) as client:
    resposta = client.get("/clientes")
    resposta.raise_for_status()
    print("Clientes:", resposta.json())

    novo = {
        "nome": "Cliente Fictício",
        "documento": "99999999999",
    }

    resposta = client.post("/clientes", json=novo)

    if resposta.status_code == 201:
        cliente = resposta.json()
        print("Criado:", cliente)

        consulta = client.get(f"/clientes/{cliente['id']}")

        if consulta.status_code == 404:
            print("Cliente não encontrado.")
        else:
            consulta.raise_for_status()
            print("Consulta:", consulta.json())
    else:
        print("Cadastro não realizado:", resposta.status_code, resposta.text)
