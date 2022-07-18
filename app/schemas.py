from pydantic import UUID4, BaseModel, EmailStr
from datetime import datetime


class create_user(BaseModel):
    email: EmailStr
    password: str


class user_out(BaseModel):
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True
