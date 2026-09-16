from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from services.user_service import create_user
from schemas import UserCreate, UserResponse, LoginRequest
from utils.token import create_access_token
from Dependencies.auth import get_current_user
from Dependencies.auth import require_admin
from models import User


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/login")
def login_user(
    login_data: LoginRequest,
    db: Session = Depends(get_db)
):
    user = authenticate_user(
        db,
        login_data.username,
        login_data.password
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    access_token = create_access_token(
        user.username
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

from models import User


@router.get("/me")
def get_me(
    current_user: User = Depends(get_current_user)
):
    return {
        "message": "You are authenticated",
        "username": current_user.username,
        "email": current_user.email
    }

@router.delete("/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    student = db.query(User).filter(
        User.id == student_id,
        User.role == "student"
    ).first()

    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    db.delete(student)
    db.commit()

    return {
        "message": f"Student with ID {student_id} has been deleted."
    }