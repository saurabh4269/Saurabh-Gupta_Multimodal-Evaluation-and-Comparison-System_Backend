from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def read_health():
    return {"status": "ok", "usage_stats": {"requests": 100}}
