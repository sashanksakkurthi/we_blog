from uuid import uuid4
from fastapi import APIRouter, Depends, status
from .. import schemas
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models
from ..authentication import oauth2
router = APIRouter(prefix="/users", tags=['Users'])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.user_out)
async def create_user(user: schemas.create_user, db: Session = Depends(get_db)):
    new_user = models.User(
        id=str(uuid4()), email=user.email, password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/")
async def verify(user:str = Depends(oauth2.get_current_user)):
    return user
