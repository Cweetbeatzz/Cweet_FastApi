from typing import List, Optional
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, File, UploadFile
from fastapi.exceptions import HTTPException
from fastapi.params import Depends
from fastapi.routing import APIRouter
from fastapi.security.oauth2 import OAuth2
from sqlalchemy.orm.session import Session
from starlette import status
from Models.beats_model import Beats
from SQL.database import get_db
from Dtos.beats_dto import BeatsDto, BeatsDtoCreate, BeatsDtoEdit, BeatsDtoResponse
from app import jwt_token_helper

router = APIRouter(prefix="/beats", tags=["Beats"])
##################################################################


@router.get("/", response_model=List[BeatsDtoResponse])
async def get_all_beats(
    db: Session = Depends(get_db),
    limit: int = 10,  # pagination
    skip: int = 0,  # skiping paginated list
    search: Optional[str] = "",  # Enables users to search for beats
):

    output = (
        db.query(Beats)
        .filter(Beats.beats_name.contains(search))
        .limit(limit)
        .offset(skip)
        .all()
    )
    return output


##################################################################

# Get all beats by a specfic user
@router.get("/user", response_model=List[BeatsDtoResponse])
async def get_all_beats(db: Session = Depends(get_db), current_user: int = Depends()):
    output = db.query(Beats).filter(Beats.user_id == current_user.id).all()
    return output


##################################################################


@router.get("/{id}")
async def get_beats_by_id(
    id: int,
    db: Session = Depends(get_db),
):
    output = db.query(Beats).filter(Beats.id == id).first()

    if not output:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    else:
        return output


##################################################################


@router.post("/Create", response_model=BeatsDtoResponse)
async def create_beats(
    beats: BeatsDtoCreate,
    db: Session = Depends(get_db),
    current_user: int = Depends(jwt_token_helper.get_current_user),
):

    output = Beats(user_id=current_user.id, **beats.dict())
    db.add(output)
    db.commit()
    db.refresh(output)

    return "Upload Successfull"


##################################################################


@router.put("/Edit/{id}", response_model=BeatsDtoResponse)
async def edit_beats(
    id: int,
    beats: BeatsDtoEdit,
    db: Session = Depends(get_db),
):
    output = db.query(Beats).filter(Beats.id == id)
    result = output.first()

    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    else:
        output.update(beats.dict(), synchronize_session=False)
        db.commit()

    return "Update Successfull"


##################################################################


@router.delete("/delete/{id}")
async def delete_beats(
    id: int,
    db: Session = Depends(get_db),
):
    output = db.query(Beats).filter(Beats.id == id)
    result = output.first()

    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    else:
        output.delete(synchronize_session=False)
        db.commit()

    return "Delete Successfull"
