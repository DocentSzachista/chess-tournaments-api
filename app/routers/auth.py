import imp
from pyexpat import version_info
from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session

from ..dependencies import get_db
from ..schemas import auth
from ..db import models
from .. import utils, oauth2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
router = APIRouter(tags=["Authentication"])

@router.post("/login")
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db) ):
    
    #{  
    #   username:
    #   password: 
    #}
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
    
    if user == None:
        raise HTTPException(status_code=403, detail="Invalid credentials")
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=403, detail="Invalid credentials")
    
    access_token = oauth2.create_access_token(data = {"user_id": user.id})

    return {
        "access_token" : access_token,
        "token_type": "bearer"
    }
