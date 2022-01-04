from fastapi.params import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm.session import Session
from Dtos.user_dto import UserLoginDto
from Models.users_model import User
from fastapi import HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from SQL.database import get_db
from app.jwt_token_helper import create_access_token
from app.passwords import compare_passwords

##################################################################


router = APIRouter(prefix="Auth", tags=["Authentication"])

##################################################################


@router.post("/login")
def user_logins(
    user: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):

    output = db.query(User).filter(User.email == user.username).first()

    if not output:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credientials"
        )

    confirm_correct_password = compare_passwords(user.password, output.password)

    if not confirm_correct_password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credientials"
        )
    else:
        access_token = create_access_token(data={"user_id": output.id})
        return {"access_token": access_token, "token_type": "bearer"}
