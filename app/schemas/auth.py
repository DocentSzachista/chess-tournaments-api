from pydantic import BaseModel, EmailStr 
from typing import Optional



class Credentials(BaseModel):
    email: EmailStr
    password : str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None