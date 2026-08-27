from fastapi import FastAPI
from app.models.db.task import Task
from app.connection.database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def get_home():
    return {"message": "server on"}