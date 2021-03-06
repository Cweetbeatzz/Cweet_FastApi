from fastapi.datastructures import UploadFile
from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP, String
from Models.users_model import User
from SQL.database import Base


class Beats(Base):
    __tablename__ = "Beats"

    id = Column(Integer, primary_key=True)
    producer = Column(String, nullable=False)
    beats_name = Column(String, nullable=False)
    beats_type_file = Column(UploadFile, nullable=False)
    beats_image_file = Column(UploadFile, nullable=False)
    genre = Column(Integer, ForeignKey("Genre.id", ondelete="CASCADE"), nullable=False)
    created_date = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    # User must be logged in to post a beat
    user_id = Column(Integer, ForeignKey("User.id", ondelete="CASCADE"), nullable=False)

    # returns the user object details
    user_details = relationship("User")
