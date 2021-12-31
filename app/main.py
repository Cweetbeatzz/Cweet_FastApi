from fastapi import FastAPI


cweetbeatz = FastAPI()

##################################################################

@cweetbeatz.get("/")
async def root():
    return {"message": "Welcome to Cweebeatz"}
