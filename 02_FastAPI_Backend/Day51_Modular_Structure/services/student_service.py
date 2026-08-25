from sqlalchemy.orm import Session

from models import Student
from schemas import StudentCreate


def create_student(
    db: Session,
    student: StudentCreate
):
    new_student = Student(
        name=student.name,
        age=student.age,
        branch=student.branch
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student


def get_students(
    db: Session,
    branch: str | None = None,
    age: int | None = None,
    name: str | None = None,
    skip: int = 0,
    limit: int = 10,
    sort_by: str = "id",
    order: str = "asc"
):
    query = db.query(Student)

    # Filtering
    if branch is not None:
        query = query.filter(Student.branch == branch)

    if age is not None:
        query = query.filter(Student.age == age)

    if name is not None:
        query = query.filter(Student.name == name)

    # Sorting
    if sort_by == "name":
        column = Student.name
    elif sort_by == "age":
        column = Student.age
    else:
        column = Student.id

    if order == "desc":
        query = query.order_by(column.desc())
    else:
        query = query.order_by(column.asc())

    # Pagination
    return query.offset(skip).limit(limit).all()

def update_student(
    db: Session,
    existing_student: Student,
    student: StudentCreate
):
    existing_student.name = student.name
    existing_student.age = student.age
    existing_student.branch = student.branch

    db.commit()
    db.refresh(existing_student)

    return existing_student