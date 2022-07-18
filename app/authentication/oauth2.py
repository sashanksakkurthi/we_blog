from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi import HTTPException, status, Depends
from sqlalchemy.orm import Session
from .. import models, database
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


SECRET_KEY = "j8YwO1ipa5zYxgpXn4hTTRPEiw1D0Wek"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    data.update({"exp": expire})
    encoded_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail=f"Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
    if token is None:
        raise credentials_exception

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("email")

        if email is None:
            raise credentials_exception
        user = db.query(models.User).filter(email == models.User.email).first()
        if not user:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    return user.email
