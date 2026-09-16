from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import Student, User
from schemas import StudentCreate, StudentResponse
from services import student_service
from dependencies import require_permission

router = APIRouter()

@router.put(
    "/{student_id}",
    response_model=StudentResponse
)
def update_student(
    student_id: int,
    student: StudentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        require_permission("student:update")
    )
):
    existing_student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if existing_student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student_service.update_student(
        db,
        existing_student,
        student
    )