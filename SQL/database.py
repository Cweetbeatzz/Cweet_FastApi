import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from enviroment import Settings

######################################################################################

SQLALCHEMY_DATABASE_URL = f"postgresql://{Settings.DATABASE_USERNAME}:{Settings.DATABASE_PASSWORD}@{Settings.DATABASE_HOSTNAME}/{Settings.DATABASE_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# This get_db function creates an open session to a CRUD request anytime a request is sent which is
# passed into the function as a parameter


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


######################################################################################

# while True:
#     try:
#         connection = psycopg2.connect(
#             host="localhost",
#             database="Cweetbeatz",
#             user="postgres",
#             password="1234567890",
#             cursor_factory=RealDictCursor,
#         )
#         cursor = connection.cursor()
#         print("Database Connection Successful")
#         ####-----BREAK------
#         break
#     except Exception as error:
#         print("Connection to Database Failed")
#         print("Error:", error)
#         time.sleep(5)
