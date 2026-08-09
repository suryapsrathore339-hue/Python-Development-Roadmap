from fastapi import FastAPI
from pydantic import BaseModel

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Student


DATABASE_URL = "sqlite:///./students.db"


engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


Base.metadata.create_all(bind=engine)


app = FastAPI()


class StudentRequest(BaseModel):
    name: str
    age: int
    branch: str


@app.get("/")
def home():
    return {"message": "FastAPI + SQLAlchemy working!"}


@app.post("/student")
def create_student(student: StudentRequest):

    db = SessionLocal()

    new_student = Student(
        name=student.name,
        age=student.age,
        branch=student.branch
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    db.close()

    return {
        "message": "Student created",
        "id": new_student.id,
        "name": new_student.name,
        "age": new_student.age,
        "branch": new_student.branch
    }


@app.get("/students")
def get_students():

    db = SessionLocal()

    students = db.query(Student).all()

    result = []

    for student in students:
        result.append({
            "id": student.id,
            "name": student.name,
            "age": student.age,
            "branch": student.branch
        })

    db.close()

    return result