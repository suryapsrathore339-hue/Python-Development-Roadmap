from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database import get_db
from models import Student
from schemas import StudentCreate, StudentResponse
from services import student_service
from dependencies.student import get_student


router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


# GET all students
@router.get("/", response_model=list[StudentResponse])
def get_students(
    branch: str | None = None,
    age: int | None = None,
    name: str | None = None,
    skip: int = 0,
    limit: int = 10,
    sort_by: str = "id",
    order: str = "asc",
    db: Session = Depends(get_db)
):
    return student_service.get_students(
        db=db,
        branch=branch,
        age=age,
        name=name,
        skip=skip,
        limit=limit,
        sort_by=sort_by,
        order=order
    )


# POST student
@router.post(
    "/",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED
)
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    return student_service.create_student(
        db=db,
        student=student
    )


# PUT student
@router.put(
    "/{student_id}",
    response_model=StudentResponse
)
def update_student(
    student_id: int,
    student: StudentCreate,
    existing_student: Student = Depends(get_student),
    db: Session = Depends(get_db)
):
    return student_service.update_student(
        db=db,
        existing_student=existing_student,
        student=student
    )


# DELETE student
@router.delete(
    "/{student_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_student(
    student_id: int,
    student: Student = Depends(get_student),
    db: Session = Depends(get_db)
):
    student_service.delete_student(
        db=db,
        student=student
    )

    return None