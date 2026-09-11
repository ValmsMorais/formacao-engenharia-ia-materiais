from fastapi import APIRouter

router = APIRouter(tags=["status"])

@router.get("/status")
def status():
    return {"status": "ok"}
