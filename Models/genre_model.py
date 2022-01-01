from sqlalchemy import Column, Integer
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP, String
from SQL.database import Base


class Genre(Base):
    __tablename__ = "Genre"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    created_date = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
