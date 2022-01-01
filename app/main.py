from fastapi import FastAPI
from Models import genre_model
from SQL.database import engine
from fastapi.middleware.cors import CORSMiddleware

from Controllers import beats_controller, genre_controller, users_controller

cweetbeatz = FastAPI()

origins = []

# cweetbeatz.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_header=["*"],
# )
##################################################################
# creates the table in the database

genre_model.Base.metadata.create_all(bind=engine)
# beats_model.Base.metadata.create_all(bind=engine)
# users_model.Base.metadata.create_all(bind=engine)

##################################################################
cweetbeatz.include_router(beats_controller.router)
cweetbeatz.include_router(genre_controller.router)
cweetbeatz.include_router(users_controller.router)


@cweetbeatz.get("/")
async def root():
    return {"message": "Welcome to Cweebeatz"}
