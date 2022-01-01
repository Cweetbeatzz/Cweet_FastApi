from datetime import datetime
from pydantic import BaseModel

##################################################################


class GenreDto(BaseModel):
    name: str


##################################################################


class GenreResponse(GenreDto):
    id: int
    created_date: datetime

    class Config:
        orm_mode = True


##################################################################


class GenreCreateDto(GenreDto):
    pass


##################################################################
