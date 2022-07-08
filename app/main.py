from enum import Enum

from fastapi import FastAPI, Path, Response
from pydantic import BaseModel, Field
from .routers import tournaments, users


app = FastAPI(title="Chess tournaments API")
app.include_router(tournaments.router)
app.include_router(users.router)



@app.get("/")
def root():
    return {"message": "I am a teapot"}

