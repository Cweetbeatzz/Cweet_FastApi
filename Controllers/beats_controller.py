from fastapi import FastAPI
from fastapi.params import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm.session import Session
from SQL.database import get_db
from Dtos.beats_dto import BeatsDto

router = APIRouter(prefix="/beats", tags=["Beats"])
##################################################################


@router.get("/")
async def get_all_beats(
    beats: BeatsDto,
    db: Session = Depends(get_db),
):
    return


##################################################################


@router.get("Beats/{id}")
async def get_beats_by_id(
    beats: BeatsDto,
    db: Session = Depends(get_db),
):
    return


##################################################################


@router.post("Beats/Create")
async def create_beats(
    beats: BeatsDto,
    db: Session = Depends(get_db),
):
    return


##################################################################


@router.put("Beats/Edit/{id}")
async def edit_beats(
    beats: BeatsDto,
    db: Session = Depends(get_db),
):
    return


##################################################################


@router.delete("Beats/delete/{id}")
async def delete_beats(
    beats: BeatsDto,
    db: Session = Depends(get_db),
):
    return
