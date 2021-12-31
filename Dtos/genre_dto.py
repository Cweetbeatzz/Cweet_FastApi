from pydantic import BaseModel


class GenreDto(BaseModel):
    name: str


class GenreCreateDto(GenreDto):
    pass


class GenreEditDto(GenreDto):
    pass
