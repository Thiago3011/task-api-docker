from pydantic import BaseModel
from datetime import datetime

class TaskCreate(BaseModel):
    title: str
    description: str | None
    
class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    completed: bool
    creation_date: datetime
    update_date: datetime | None