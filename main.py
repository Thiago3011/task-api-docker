from fastapi import FastAPI
from app.models.db.task import Task
from app.connection.database import Base, engine
from app.routes import task_routes
from app.config import APP_ENV

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(task_routes.router)

@app.get("/")
def get_home():
    return {"message": "server on"}

@app.get("/environment")
def get_environment():
    return {"environment": APP_ENV}