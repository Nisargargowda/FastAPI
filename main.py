from fastapi import FastAPI
from routers import users
import models
from database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)

@app.get("/")
def root():
    return "Learning FastAPI"