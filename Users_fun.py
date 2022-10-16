from schemas import UserCreate
from hashing import get_password_hash
from sqlalchemy.orm import Session
from models import User


def create_new_user(user:UserCreate,db:Session):
    user = User(username=user.username,
        email = user.email,
        hashed_password=get_password_hash(user.password),
        is_superuser=user.is_superuser
        )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
