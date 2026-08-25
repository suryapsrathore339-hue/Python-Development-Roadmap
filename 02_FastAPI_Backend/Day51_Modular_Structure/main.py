from fastapi import FastAPI

from database import engine, Base
import models

from config.settings import settings

from routers.auth import router as auth_router


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title=settings.APP_NAME
)


app.include_router(auth_router)