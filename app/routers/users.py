from fastapi import APIRouter, HTTPException, Path, Response, Depends
from sqlalchemy.orm import Session

from ..schemas import UserDB
from ..dependencies import get_db
from ..db.crud import user
 

router = APIRouter(
    prefix = "/users",
    tags = ["users"]
)

@router.get("/")
def get_user(db: Session = Depends(get_db)):
    return user.read_users(db)

@router.post("/")
def register_user(new_user :UserDB, db: Session = Depends(get_db)):
    created_user = user.create_user(db , new_user)
    # fake_db.append(new_user.__dict__)
    return created_user

@router.put("/")
def update_user_data(updated_user: UserDB):
    return {"message": "Update user"}

@router.delete("/", status_code=204)
def delete_user(id: int, db: Session = Depends(get_db)):
    return user.remove_user(db, id)
    