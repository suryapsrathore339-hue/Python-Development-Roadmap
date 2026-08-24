from fastapi import FastAPI

from database import engine, Base
import models

from config.settings import settings

from routers.students import router as student_router


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title=settings.APP_NAME
)


app.include_router(student_router)