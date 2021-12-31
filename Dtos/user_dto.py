from pydantic import BaseModel
from pydantic.networks import EmailStr


class UserCreateDto(BaseModel):
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
