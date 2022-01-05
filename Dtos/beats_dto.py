from pydantic import BaseModel
from Dtos.user_dto import UserResponse


##################################################################


class BeatsDto(BaseModel):
    beats_name: str
    producer: str
    beat_file: str
    image_file: str
    genre: str


##################################################################


class BeatsDtoResponse(BeatsDto):
    id: int
    created_date: str
    updated_date: str
    user: UserResponse


##################################################################


class BeatsDtoCreate(BeatsDto):
    pass


##################################################################


class BeatsDtoEdit(BeatsDto):
    pass


##################################################################
