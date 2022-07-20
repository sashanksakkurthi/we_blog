from uuid import uuid4
from fastapi import APIRouter,Depends,status
from ..oauth2 import get_current_user
from ..database import get_db
from sqlalchemy.orm import Session
from .. import models
from .. import schemas

router = APIRouter(prefix="/api/v1")


@router.post("/create-post/",status_code=status.HTTP_201_CREATED)
async def user_posts(create_post:schemas.CreatePost ,current_user:dict = Depends(get_current_user),db:Session = Depends(get_db) ):
    post = models.Post(id=str(uuid4()),user_id = current_user.hash,content = create_post.content,hash = str(uuid4()))
    db.add(post)
    db.commit()
    db.refresh(post)
    return post


@router.get("/")
async def get_all_post():
    pass