from typing import List
from fastapi import Response, status, HTTPException
from fastapi.params import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm.session import Session

from SQL.database import get_db

from Dtos.genre_dto import GenreCreateDto, GenreDto, GenreResponse
from Models.genre_model import Genre


router = APIRouter(prefix="/genre", tags=["Genre"])
##################################################################


@router.get("/", response_model=List[GenreResponse])
async def get_all_genre(db: Session = Depends(get_db)):
    output = db.query(Genre).all()
    return output


##################################################################


@router.get("/{id}", response_model=GenreResponse)
async def get_genre_by_id(
    id: int,
    db: Session = Depends(get_db),
):
    output = db.query(Genre).filter(Genre.id == id).first()

    if not output:
        return False
    else:
        return output


##################################################################


@router.post("/create")
async def create_genre(
    genre_dto: GenreCreateDto,
    db: Session = Depends(get_db),
):
    output = Genre(**genre_dto.dict())
    db.add(output)
    db.commit()
    db.refresh(output)

    return output


##################################################################


@router.put("/edit/{id}")
async def edit_genre(
    id: int,
    genre_dto: GenreCreateDto,
    db: Session = Depends(get_db),
):
    output = db.query(Genre).filter(Genre.id == id)
    result = output.first()

    if result == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Genre not Found"
        )

    output.update(genre_dto.dict(), synchronize_session=False)
    db.commit()

    return "Update Successfull"


##################################################################


@router.delete("/delete/{id}")
async def delete_genre(
    id: int,
    db: Session = Depends(get_db),
):
    output = db.query(Genre).filter(Genre.id == id)

    if output.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Genre not Found"
        )
    else:
        output.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
