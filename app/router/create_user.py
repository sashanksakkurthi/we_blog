from uuid import uuid4
from fastapi import APIRouter, Depends, status
from .. import schemas
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models
from ..utils import hashing

router = APIRouter(prefix="/api/v1/user", tags=['user'])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
async def create_user(user: schemas.CreateUser, db: Session = Depends(get_db)):
    
    password = hashing.hash_password(user.password) 
    new_user = models.User(
        id=str(uuid4()), email=user.email,hash = str(uuid4()),
        name=user.name,password=password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
