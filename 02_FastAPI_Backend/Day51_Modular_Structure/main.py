from fastapi import FastAPI

from database import engine, Base

# Import models so SQLAlchemy registers the tables
import models

from routers.students import router as student_router


Base.metadata.create_all(bind=engine)


app = FastAPI()


app.include_router(student_router)