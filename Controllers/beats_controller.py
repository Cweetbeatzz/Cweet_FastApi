from typing import List
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, File, UploadFile
from fastapi.exceptions import HTTPException
from fastapi.params import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm.session import Session
from starlette import status
from Models.beats_model import Beats
from SQL.database import get_db
from Dtos.beats_dto import BeatsDto, BeatsDtoCreate, BeatsDtoEdit, BeatsDtoResponse

router = APIRouter(prefix="/beats", tags=["Beats"])
##################################################################


@router.get("/", response_model=List[BeatsDtoResponse])
async def get_all_beats(
    db: Session = Depends(get_db),
):
    output = db.query(Beats).all()
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
):
    output = Beats(**beats.dict())
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
