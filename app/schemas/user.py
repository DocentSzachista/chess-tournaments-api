
from pydantic import BaseModel, Field, EmailStr
from .enums import Gender
from datetime import date

class UserBase(BaseModel):
     firstname:  str = Field( 
          title = "Person's first name", 
          max_length = 50,
          example = "Alice"
          ) 
     lastname: str = Field(
          title = "Person's last name", 
          max_length = 50,
          example = "Doe"
          )
     email: EmailStr
     gender : Gender = Field(
          title = "Person's gender. there is no place for Apache's, etc. You must provide biological gender"
          )
     birthYear: date = Field(
          title = "Date of person's birth", 
          description = "Lets try to keep it in format YYYY/MM/DD or DD/MM/YYYY"
          )
     rankPZszach : int = Field(
          default = 1000,  
          title = "Polish ranking",
          description = "Its value doesn't fall, it can only rise, but it's not our concern here tbh.",
          ge = 1000
          )
  

class UserCreate(UserBase):
     password : str = Field(title = "Haslo a co")
     blitz : int = Field(title = "Blitz ranking", default= 1000, ge = 0)
     rapid : int = Field(title = "Rapid ranking", default= 1000, ge = 0)
     standard : int = Field(title = "Classic ranking", default= 1000, ge = 0)      

class UserOut(UserBase):
     id: int 
     class Config:
          orm_mode = True

