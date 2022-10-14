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
    