from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Depends
from pydantic.main import Model
from sqlalchemy.orm.session import Session

from database import get_db

from ..Dtos.genre_dto import GenreCreateDto, GenreDto, GenreEditDto
from ..Models.genre_model import Genre


cweetbeatz = FastAPI()

##################################################################


@cweetbeatz.get("/")
async def get_all_genre(genre_dto: GenreDto, db: Session = Depends(get_db)):
    output = db.query(Genre).all()
    return output


##################################################################


@cweetbeatz.get("Genre/{id}")
async def get_genre_by_id(
    id: int,
    genre_dto: GenreDto,
    db: Session = Depends(get_db),
):
    output = db.query(Genre).filter(genre_dto.id == id).first()

    if not output:
        return False
    else:
        return output


##################################################################


@cweetbeatz.post("Genre/Create")
async def create_genre(
    genre_dto: GenreCreateDto,
    db: Session = Depends(get_db),
):
    output = Genre(**genre_dto.dict())
    db.add(output)
    db.commit()
    db.refresh()

    return output


##################################################################


@cweetbeatz.put("Genre/Edit/{id}")
async def edit_genre(
    id: int,
    genre_dto: GenreEditDto,
    db: Session = Depends(get_db),
):
    output = db.query(Genre).filter(genre_dto.id == id)

    if output.first() == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Genre not Found"
        )
    else:
        output.update(genre_dto.dict(), synchronize_session=False)
        db.commit()

    return Response(status_code=status.HTTP_200_OK)


##################################################################


@cweetbeatz.delete("Genre/delete/{id}")
async def delete_genre(
    id: int,
    genre_dto: GenreDto,
    db: Session = Depends(get_db),
):
    output = db.query(Genre).filter(genre_dto.id == id)

    if output.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Genre not Found"
        )
    else:
        db.delete(synchronize_session=False)
        db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
