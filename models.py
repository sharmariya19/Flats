from database import Base
from sqlalchemy import Column,Integer,Float, String,Boolean, ForeignKey
from sqlalchemy.orm import relationship

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

 
# class Tenants(Base):
#     __tablename__ = "tenants"

#     id = Column(Integer,primary_key=True,index=True)
#     tenant_name = Column(String,nullable=False)
#     company_name = Column(String,nullable=False)
#     contact = Column(String,nullable=False)
#     address = Column(String,nullable=False)

    # flats = relationship(Tenants, back_populates="tenants")

class FlatAssignment(Base):
    __tablename__ = "flat_assignment"

    id = Column(Integer,primary_key=True,index=True)
    flat_id = Column(Integer,ForeignKey("flats.id"))
    user_id = Column(Integer,ForeignKey("users.id"))
    rent = Column(Integer)
    lease_time = Column(Integer)
    # tenant_name = Column(Integer,ForeignKey("tenants.tenant_name"))

  
    
    # flats = relationship("Flats")
    # tenants = relationship("Tenants")
    # tenants = relationship(Tenants, back_populates="flats")
    


