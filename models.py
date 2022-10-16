from database import Base
from sqlalchemy import Column,Integer,Float, String,Boolean, ForeignKey

class Flats(Base):
    __tablename__ = "flats"

    id = Column(Integer, primary_key = True, index= True)
    status = Column(String , nullable=False, default = "available")
    rooms = Column(Integer,nullable=False)
    halls = Column(Integer,nullable=False)
    floor_no = Column(Integer,nullable=False)
    monthly_rent = Column(Integer)
    sqft_area = Column(Float,nullable=False)
    

class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String,unique=True,nullable=False)
    email = Column(String,nullable=False,unique=True,index=True)
    hashed_password = Column(String,nullable=False)
    is_superuser = Column(Boolean(),default=False)
    
