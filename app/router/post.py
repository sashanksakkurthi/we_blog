from uuid import uuid4
from fastapi import APIRouter,Depends, HTTPException,status
from ..oauth2 import get_current_user
from ..database import get_db
from sqlalchemy.orm import Session
from .. import models
from .. import schemas
from sqlalchemy import func

router = APIRouter(prefix="/api/v1")


@router.post("/create-post/",status_code=status.HTTP_201_CREATED,response_model=schemas.PostOut)
async def user_posts(create_post:schemas.CreatePost ,current_user:dict = Depends(get_current_user),db:Session = Depends(get_db) ):
    post = models.Post(id=str(uuid4()),user_id = current_user.hash,content = create_post.content,hash = str(uuid4()))
    db.add(post)
    db.commit()
    db.refresh(post)
    return post


@router.get("/posts/")
async def get_all_post(current_user:dict = Depends(get_current_user),db:Session = Depends(get_db)):
    posts = db.query(models.Post,db.query(models.User.id).label("user")).join(
                 models.User, models.User.hash == models.Post.user_id).group_by(models.Post.id).all()
    
    return posts
    

@router.post("/delete-posts/",status_code=status.HTTP_202_ACCEPTED)
async def delete_post(delete_post_schema:schemas.DeletePost,current_user:dict = Depends(get_current_user),db:Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.hash == delete_post_schema.hash).delete(synchronize_session=False)
    db.commit()
    return post_query

@router.post("/delete-all-posts/",status_code=status.HTTP_202_ACCEPTED)
async def delete_post(current_user:dict = Depends(get_current_user),db:Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.user_id == current_user.hash).delete(synchronize_session=False)
    db.commit()
    return post_query