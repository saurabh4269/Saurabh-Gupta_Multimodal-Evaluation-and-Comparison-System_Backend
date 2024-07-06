from fastapi import APIRouter, HTTPException, Depends
from app.models import TaskInput
from app.services.model_service import get_models, evaluate_text
from fastapi_limiter.depends import RateLimiter

router = APIRouter()

@router.post("/evaluate", dependencies=[Depends(RateLimiter(times=10, seconds=60))])
async def evaluate(task_input: TaskInput):
    task = task_input.task
    text = task_input.text

    models = get_models(task)
    if not models:
        raise HTTPException(status_code=400, detail="Task not supported")

    results = evaluate_text(models, text)
    return results
