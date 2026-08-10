from fastapi import FastAPI, Depends
from pydantic import BaseModel

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

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


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


app = FastAPI()


class StudentRequest(BaseModel):
    name: str
    age: int
    branch: str


@app.get("/students")
def get_students(db: Session = Depends(get_db)):

    students = db.query(Student).all()

    result = []

    for student in students:
        result.append({
            "id": student.id,
            "name": student.name,
            "age": student.age,
            "branch": student.branch
        })

    return result


@app.post("/student")
def create_student(
    student: StudentRequest,
    db: Session = Depends(get_db)
):
    new_student = Student(
        name=student.name,
        age=student.age,
        branch=student.branch
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return {
        "message": "Student created",
        "id": new_student.id,
        "name": new_student.name,
        "age": new_student.age,
        "branch": new_student.branch
    }

@app.put("/student/{student_id}")
def update_student(
    student_id: int,
    student: StudentRequest,
    db: Session = Depends(get_db)
):
    existing_student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if existing_student is None:
        return {"message": "Student not found"}

    existing_student.name = student.name
    existing_student.age = student.age
    existing_student.branch = student.branch

    db.commit()
    db.refresh(existing_student)

    return {
        "message": "Student updated",
        "id": existing_student.id,
        "name": existing_student.name,
        "age": existing_student.age,
        "branch": existing_student.branch
    }

@app.delete("/student/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if student is None:
        return {"message": "Student not found"}

    db.delete(student)
    db.commit()

    return {
        "message": "Student deleted",
        "id": student_id
    }