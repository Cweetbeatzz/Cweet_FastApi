from fastapi import FastAPI
from fastapi.params import Depends
from sqlalchemy.orm.session import Session

from database import get_db
from ..Dtos.user_dto import UserCreate


cweetbeatz = FastAPI()

##################################################################


@cweetbeatz.get("/")
async def get_all_user(
    beats: UserCreate,
    db: Session = Depends(get_db),
):
    return


##################################################################


@cweetbeatz.get("User/{id}")
async def get_user_by_id(
    beats: UserCreate,
    db: Session = Depends(get_db),
):
    return


##################################################################


@cweetbeatz.post("User/Create")
async def create_user(
    beats: UserCreate,
    db: Session = Depends(get_db),
):
    return


##################################################################


@cweetbeatz.put("User/Edit/{id}")
async def edit_user(
    beats: UserCreate,
    db: Session = Depends(get_db),
):
    return


##################################################################


@cweetbeatz.delete("User/delete/{id}")
async def delete_user(beats: UserCreate):
    return
