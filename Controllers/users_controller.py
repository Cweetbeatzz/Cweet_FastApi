from typing import List
from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from fastapi.params import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm.session import Session
from starlette import status
from starlette.responses import Response
from Models.users_model import User
from SQL.database import get_db
from Dtos.user_dto import UserCreateDto, UserEditDto, UserResponse


router = APIRouter(prefix="/users", tags=["Users"])
##################################################################


@router.get("/", response_model=List[UserResponse])
async def get_all_user(
    db: Session = Depends(get_db),
):
    output = db.query(User).all()
    return output


##################################################################


@router.get("/{id}", response_model=UserResponse)
async def get_user_by_id(
    id: int,
    db: Session = Depends(get_db),
):
    output = db.query(User).filter(User.id == id).first()

    if not output:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not Found"
        )
    else:
        return output


##################################################################


@router.post("User/Create")
async def create_user(
    user: UserCreateDto,
    db: Session = Depends(get_db),
):
    output = User(**user.dict())
    db.add(output)
    db.commit()
    db.refresh(output)

    return "Successfull"


##################################################################


@router.put("/Edit/{id}", response_model=UserResponse)
async def edit_user(
    id: int,
    beats: UserEditDto,
    db: Session = Depends(get_db),
):
    output = db.query(User).filter(User.id == id)
    result = output.first()

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not Found"
        )
    else:
        output.update(beats.dict(), synchronize_session=False)
        db.commit()

    return "Update Successfull"


##################################################################


@router.delete("/delete/{id}")
async def delete_user(id: int, db: Session = Depends(get_db)):
    output = db.query(User).filter(User.id == id)
    result = output.first()

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not Found"
        )
    else:
        output.delete(synchronize_session=False)
        db.commit()

    return "Delete Successfull"
