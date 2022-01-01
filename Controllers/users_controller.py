from fastapi import FastAPI
from fastapi.params import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm.session import Session

from SQL.database import get_db
from Dtos.user_dto import UserCreateDto

router = APIRouter(prefix="/users", tags=["Users"])
##################################################################


@router.get("/")
async def get_all_user(
    beats: UserCreateDto,
    db: Session = Depends(get_db),
):
    return


##################################################################


@router.get("User/{id}")
async def get_user_by_id(
    beats: UserCreateDto,
    db: Session = Depends(get_db),
):
    return


##################################################################


@router.post("User/Create")
async def create_user(
    beats: UserCreateDto,
    db: Session = Depends(get_db),
):
    return


##################################################################


@router.put("User/Edit/{id}")
async def edit_user(
    beats: UserCreateDto,
    db: Session = Depends(get_db),
):
    return


##################################################################


@router.delete("User/delete/{id}")
async def delete_user(beats: UserCreateDto):
    return
