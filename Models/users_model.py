from sqlalchemy.sql.sqltypes import TIMESTAMP
from database import Base
from sqlalchemy import Column, Integer, String, DATETIME, Boolean
from sqlalchemy.sql.expression import text


class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, nullable=False)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    address = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    state = Column(String, nullable=False)
    country = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    password = Column(String, nullable=False)
    confirmpassword = Column(String, nullable=False)
    created_date = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
