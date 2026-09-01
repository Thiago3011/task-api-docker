from app.models.db.task import Task as TaskDb
from app.models.schemas.task import TaskCreate
from sqlalchemy import select
from sqlalchemy.orm import Session

def create_task(task: TaskCreate, db: Session) -> None:
    task = TaskDb(
        title=task.title,
        description=task.description
    )
    
    db.add(task)
    db.commit()
    db.refresh(task)
    
    return {"message": "Taks created succeffuly"}

def get_tasks(db: Session) -> list[dict]:
    tasks = db.execute(select(TaskDb))
    
    response = tasks.scalars().all()
    
    return response