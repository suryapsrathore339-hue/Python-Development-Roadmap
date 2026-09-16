from datetime import datetime, timedelta, timezone

import jwt

from config.settings import settings


ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(username: str) -> str:
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": username,
        "exp": expire
    }

    token = jwt.encode(
        payload,
        settings.JWT_SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token