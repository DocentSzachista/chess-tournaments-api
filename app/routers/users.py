from fastapi import APIRouter, HTTPException, Path, Response, Depends
from sqlalchemy.orm import Session

from ..schemas.user import UserBase, UserCreate, UserDetails, UserOut
from ..dependencies import get_db
from ..db.crud import user
from ..utils import hash_pwd

router = APIRouter(
    prefix = "/users",
    tags = ["users"]
)


@router.get("/{id}", response_model=UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.get_user(db, id)

@router.post("/", response_model=UserOut)
def register_user(new_user: UserCreate, db: Session = Depends(get_db)):
    new_user.password = hash_pwd(new_user.password)
    created_user = user.create_user(db , new_user)
    return created_user

@router.put("/")
def update_user_data(updated_user: UserDetails):
    return {"message": "Update user"}

@router.delete("/", status_code=204)
def delete_user(id: int, db: Session = Depends(get_db)):
    return user.remove_user(db, id)

