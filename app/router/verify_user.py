from fastapi import APIRouter, Depends,status
from ..oauth2 import get_current_user
from ..schemas import VerifyUser

router = APIRouter(prefix="/api/v1/verify")

@router.post("/",status_code=status.HTTP_202_ACCEPTED,response_model=VerifyUser)
async def verify_user(current_user:dict = Depends(get_current_user)):
    return current_user
