
from datetime import datetime,timedelta
from typing import Optional
from jose import jwt
from models import User
from sqlalchemy.orm import Session
from hashing import verify_password

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, "sheersh", algorithm="HS256")
    return encoded_jwt

def get_user(username:str,db: Session):
    user = db.query(User).filter(User.email == username).first()
    return user

def authenticate_user(username: str, password: str,db: Session):
    user = get_user(username=username,db=db)
    print(user)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

