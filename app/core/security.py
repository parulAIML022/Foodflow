import jwt
from datetime import datetime, timedelta, timezone
from app.core.config import settings
from pwdlib import PasswordHash
password_hash = PasswordHash.recommended()
def hash_password(password: str) -> str:
    return password_hash.hash(password)
def verify_password(password: str, hashed_password: str) -> bool:
    return password_hash.verify(password, hashed_password)
def create_access_token(user_id: int) -> str:

    payload = {
        "user_id": user_id,
        "exp": datetime.now(timezone.utc) + timedelta(hours=1)
    }

    token = jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

    return token