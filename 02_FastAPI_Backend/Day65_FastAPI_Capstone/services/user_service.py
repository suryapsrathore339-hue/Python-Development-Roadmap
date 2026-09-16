from sqlalchemy.orm import Session

from models import User
from schemas import UserCreate
from utils.security import hash_password, verify_password

def authenticate_user(
    db: Session,
    username: str,
    password: str
):
    user = db.query(User).filter(
        User.username == username
    ).first()

    if user is None:
        return None

    if not verify_password(
        password,
        user.hashed_password
    ):
        return None

    return user


def create_user(
    db: Session,
    user: UserCreate
):
    existing_user = db.query(User).filter(
        (User.username == user.username) |
        (User.email == user.email)
    ).first()

    if existing_user:
        return None

    hashed_password = hash_password(user.password)

    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user