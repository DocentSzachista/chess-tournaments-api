from enum import Enum
from fastapi import Depends, FastAPI, Path, Response
from pydantic import BaseModel, Field

from .routers import tournaments, users
from .db.database import SessionLocal, engine
from .db import models
from .dependencies import oauth2_scheme

app = FastAPI(title="Chess tournaments API")
app.include_router(tournaments.router)
app.include_router(users.router)
models.Base.metadata.create_all(bind=engine)



@app.get("/")
def root(token: str = Depends(oauth2_scheme)):
    return {"token": token}

