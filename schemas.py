from typing import List
from pydantic import BaseModel, EmailStr
from typing import Optional


class Flat_create(BaseModel):
    status: str
    floor_no: int
    rooms: int
    halls: int
    sqft_area: int
    monthly_rent:int



class show_flat(BaseModel):
    id: int
    status: str
    floor_no: int
    rooms: int
    halls: int
    sqft_area: int
    monthly_rent:int
    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    username: str
    email : EmailStr
    password : str
    is_superuser : bool


class ShowUser(BaseModel):   #new
    username : str 
    email : EmailStr
    is_superuser : bool
    class Config():  #tells pydantic to convert even non dict obj to json
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str
