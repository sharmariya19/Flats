from schemas import flat_assign, flat_assigned
from sqlalchemy.orm import Session
from models import FlatAssignment
from fastapi import HTTPException,status
from Flats_fun import update_status_by_id


def flatassign(obj: flat_assign,db: Session ):
    flat = FlatAssignment(**obj.dict())
    update_status_by_id(flat.flat_id,db)
    db.add(flat)
    db.commit()
    db.refresh(flat)
    return flat

def flat_assign_details(db:Session):
    flats=db.query(FlatAssignment).all()
    return flats

def get_details_byID(id:int , db:Session):
    flat=db.query(FlatAssignment).get(id)
    return flat

