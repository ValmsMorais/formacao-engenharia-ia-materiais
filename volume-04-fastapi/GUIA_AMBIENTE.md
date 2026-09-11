# Preparando o ambiente

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

Acesse:
- API: http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

Nunca publique `.env` real.
