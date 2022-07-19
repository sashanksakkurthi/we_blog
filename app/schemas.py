import email
from pydantic import UUID4, BaseModel, EmailStr
from datetime import datetime


class CreateUser(BaseModel):
    email: EmailStr
    name:str
    password: str


class UserOut(BaseModel):
    email: EmailStr
    name:str

    class Config:
        orm_mode = True

class GetCurrentUser(BaseModel):
    name:str
    email:EmailStr