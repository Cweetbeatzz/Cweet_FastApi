from sqlalchemy import Column, Integer
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP, String
from database import Base


class Beats(Base):
    __tablename__ = "Beats"

    id = Column(Integer, primary_key=True)
    producer = Column(String, nullable=False)
    beats_title = Column(String, nullable=False)
    beats_name = Column(String, nullable=False)
    beats_file = Column(String, nullable=False)
    beats_image_file = Column(String, nullable=False)
    genre = Column(Integer, ForeignKey("Genre.id", ondelete="CASCADE"), nullable=False)
    created_date = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
