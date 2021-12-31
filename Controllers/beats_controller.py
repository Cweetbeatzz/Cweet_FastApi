from fastapi import FastAPI
from fastapi.params import Depends
from sqlalchemy.orm.session import Session

from database import get_db
from ..Dtos.beats_dto import Beats


cweetbeatz = FastAPI()

##################################################################


@cweetbeatz.get("/")
async def get_all_beats(
    beats: Beats,
    db: Session = Depends(get_db),
):
    return


##################################################################


@cweetbeatz.get("Beats/{id}")
async def get_beats_by_id(
    beats: Beats,
    db: Session = Depends(get_db),
):
    return


##################################################################


@cweetbeatz.post("Beats/Create")
async def create_beats(
    beats: Beats,
    db: Session = Depends(get_db),
):
    return


##################################################################


@cweetbeatz.put("Beats/Edit/{id}")
async def edit_beats(
    beats: Beats,
    db: Session = Depends(get_db),
):
    return


##################################################################


@cweetbeatz.delete("Beats/delete/{id}")
async def delete_beats(
    beats: Beats,
    db: Session = Depends(get_db),
):
    return
