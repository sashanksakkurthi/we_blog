from fastapi import APIRouter, Depends, HTTPException, status, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from ..database import get_db
from sqlalchemy.orm import Session
from .. import models
from . import oauth2


router = APIRouter(prefix="/login", tags=["Authentication"])


@router.post("/")
async def get_token(response: Response, form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    user = db.query(models.User).filter(
        models.User.email == form_data.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid email or password")
    if user.password != form_data.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid email or password")

    access_token = oauth2.create_access_token(data={"email": user.email})

    response.set_cookie(key="access_token",
                        value=f"Bearer {access_token}", httponly=True)

    return {status.HTTP_200_OK}
