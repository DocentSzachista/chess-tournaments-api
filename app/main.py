from fastapi import Depends, FastAPI

from .routers import tournaments, users, auth
from .db.database import engine
from .db import models
# from .dependencies import oauth2_scheme

app = FastAPI(title="Chess tournaments API")
app.include_router(tournaments.router)
app.include_router(users.router)
app.include_router(auth.router)
models.Base.metadata.create_all(bind=engine)




# @app.get("/")
# def root(token: str = Depends(oauth2_scheme)):
#     return {"token": token}

