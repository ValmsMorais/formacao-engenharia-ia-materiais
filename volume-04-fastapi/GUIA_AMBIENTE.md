# Preparando o ambiente

Execute os comandos a partir da pasta do projeto:

```powershell
cd projeto/api-transacoes
```

## Windows
```powershell
py -m venv .venv
.venv\Scripts\activate
py -m pip install -r requirements.txt
```

## Executar
```powershell
fastapi dev app/main.py
```

O projeto entregue é uma estrutura inicial e possui o endpoint `/api/v1/status`. Antes de executar os exemplos que criam ou consultam clientes, implemente os endpoints de clientes apresentados no PDF.

Acesse:
- API: http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

Nunca publique `.env` real.
