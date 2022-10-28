from datetime import timedelta, datetime
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from models.user import User
from hashing import Hasher
from jose import jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

router = APIRouter()

@router.post("/token", tags=["login"])
def retrieve_token(form_data:OAuth2PasswordRequestForm=Depends(), db:Session=Depends(get_db)):     #retrieve token after authentication
    user = db.query(User).filter(form_data.username==User.email).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "Invalid Username")
    if not Hasher.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "Invalid Password")
    # if user == "riya@gkmit.co":
    expire = datetime.utcnow() + timedelta(minutes=30)
    data = {"sub": form_data.username}
    data.update({"exp":expire})
    jwt_token = jwt.encode(data, "riya", algorithm="HS256")

    return {"access_token":jwt_token, "token_type":"bearer"}