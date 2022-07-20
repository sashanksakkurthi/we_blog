from pydantic import UUID4, BaseModel, EmailStr

# used in post route
class CreatePost(BaseModel):
    content:str

# used in post route
class PostOut(BaseModel):
    content:str
    created_at:str
    publish:bool
    hash:str

# used in create_user route
class CreateUser(BaseModel):
    email: EmailStr
    name:str
    password: str

    class Config:
        orm_mode = True

# used in create_user route
class UserOut(BaseModel):
    email: EmailStr
    name:str
    hash:str

    class Config:
        orm_mode = True

# used in verify_user route
class VerifyUser(BaseModel):
    name:str
    email:EmailStr
    verified:bool
    hash:UUID4
    active:bool

    class Config:
        orm_mode = True