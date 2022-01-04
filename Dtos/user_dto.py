from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from pydantic.networks import EmailStr


class UserBase(BaseModel):
    firstname: str
    lastname: str
    username: str
    email: EmailStr
    address: str
    phone: str
    state: str
    country: str
    gender: str
    password: str
    confirmpassword: str


##################################################################


class UserCreateDto(UserBase):
    pass


##################################################################
class UserEditDto(UserBase):
    pass


##################################################################
class UserLoginDto(UserBase):
    email: EmailStr
    password: str


##################################################################
class Token(BaseModel):
    access_token: str
    token_type: str


##################################################################
class TokenData(BaseModel):
    id: Optional[str] = None


##################################################################
class UserResponse(UserBase):
    id: int
    created_date: datetime

    class Config:
        orm_mode = True


##################################################################
