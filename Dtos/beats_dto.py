from pydantic import BaseModel


class BeatsDto(BaseModel):
    id: int
    name: str
    beat_file: str
    image_file: str
    genre: str
    created_date: str
    updated_date: str
