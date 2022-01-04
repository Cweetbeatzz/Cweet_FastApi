from datetime import datetime, timedelta
from jose import jwt
from jose.exceptions import JWTError
from jose import jwt
from fastapi import HTTPException, status
from fastapi.params import Depends
from fastapi.security.oauth2 import OAuth2PasswordBearer
from Dtos.user_dto import TokenData
from enviroment import settings


oauth2 = OAuth2PasswordBearer(tokenUrl="login")

JWT_SECRET_KEY = settings.JWT_SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})

    encoded_token = jwt.encode(to_encode, JWT_SECRET_KEY, algorithms=ALGORITHM)
    return encoded_token


def verify_access_token(token: str, credientials_execption):
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("user_id")
        if id is None:
            raise credientials_execption
        token_data = TokenData(id=id)
    except JWTError:
        raise credientials_execption
    return token_data


def get_current_user(token: str = Depends(oauth2)):
    credientials_execpetion = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=f"Could not Validate",
        headers={"WWW.Authenticate": "Bearer"},
    )
    return verify_access_token(token, credientials_execpetion)
