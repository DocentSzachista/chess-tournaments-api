from tokenize import group
from fastapi import APIRouter, Path, Response
from ..schemas import UserDB
router = APIRouter(
    prefix = "/users",
    tags = ["users"]
)
fake_db = []

# TODO: implement after providing support to database

@router.post("/")
def register_user(new_user :UserDB):
    fake_db.append(new_user.__dict__)
    return new_user

@router.put("/")
def update_user_data(updated_user: UserDB):
    return {"message": "Update user"}

@router.delete("/")
def delete_user(user_to_delete: UserDB):
    return {"Delete": "Delete user"}