from sqlalchemy.orm import Session

from app.repositories.user_repository import create_user, get_user_by_email
from app.core.security import hash_password
from app.core.security import verify_password, create_access_token


def register_user(
    db: Session,
    name: str,
    email: str,
    password: str
):
    existing_user = get_user_by_email(db, email)

    if existing_user:
        raise ValueError("Email already registered")

    password_hash = hash_password(password)

    user = create_user(
        db=db,
        name=name,
        email=email,
        password_hash=password_hash
    )

    return user
def login_user(
    db: Session,
    email: str,
    password: str
):
    user = get_user_by_email(db, email)

    if not user:
        raise ValueError("Invalid email or password")

    if not verify_password(password, user.password_hash):
        raise ValueError("Invalid email or password")

    token = create_access_token(user.id)

    return token