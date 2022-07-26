from fastapi import HTTPException, Response
from sqlalchemy.orm import Session 
from .. import models
from ...schemas import user

def create_user(db: Session, user: user.UserCreate):
    

    db_user = models.User(
        firstname = user.firstname,
        lastname = user.lastname,
        email = user.email,
        gender = user.gender,
        birthYear = user.birthYear,
        rankPZszach = user.rankPZszach,
        password = user.password 
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    db_rankings = models.FIDERanking(
        standard = user.standard,
        blitz = user.blitz,
        rapid = user.rapid,
        user_id = db_user.id
    )
    db.add(db_rankings)
    db.commit()
    db.refresh(db_rankings)
    return db_user
def remove_user(db: Session, id: int):
    
    user = db.query(models.User).filter(models.User.id == id)
    if user.first() == None:
        raise HTTPException(status_code=404, detail=f"User with given id={id} not found")
    user.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=204)

def get_user(db: Session, id: int):
    user = db.query(models.User).filter(models.User.id == id).first()
    if user == None:
        raise HTTPException(status_code=404, detail=f"User with given id={id} not found")
    return user

def update_user(db: Session, user_id: int,   user_updated:  user.UserDetails ):
    
    query = db.query( models.User ).filter(
        models.User.id == user_id )
    user = query.first()

    if not user : 
        raise HTTPException(status_code=404, detail=f"User with given id={id} not found")
    
    query.update(user_updated.dict(), synchronize_session=False)
    db.commit()



# TODO: delete   
def read_users(db: Session, skip: int = 0 , limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()