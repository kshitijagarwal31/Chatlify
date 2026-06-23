from fastapi import FastAPI
from routes import router
from database import engine, Base

app = FastAPI()

app.include_router(router)


