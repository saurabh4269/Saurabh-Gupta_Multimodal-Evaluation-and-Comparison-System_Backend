from pydantic import BaseModel
from typing import List, Dict

class TaskInput(BaseModel):
    text: str
    task: str

class BenchmarkInput(BaseModel):
    dataset: List[Dict[str, str]]
    task: str
