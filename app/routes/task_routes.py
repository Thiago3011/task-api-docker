from fastapi import APIRouter, Depends
from app.connection.database import get_db
from sqlalchemy.orm import Session
from app.models.schemas.task import TaskCreate, TaskResponse
from app.services import task_services

router = APIRouter(
    prefix="/task",
    tags=["task"]
)

@router.get("/", response_model=list[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    return task_services.get_tasks(db)

@router.post("/")
def register_task(new_task: TaskCreate, db: Session = Depends(get_db)):
    return task_services.create_task(new_task, db)