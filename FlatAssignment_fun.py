from schemas import flat_assign, flat_assigned
from sqlalchemy.orm import Session
from models import FlatAssignment, Flats
from fastapi import HTTPException,status
from Flats_fun import update_status_by_id, check_status


def flatassign(obj: flat_assign,db: Session ):
    if check_status(obj.flat_id, db) is True:
        flat = FlatAssignment(**obj.dict())
        update_status_by_id(flat.flat_id,db)
        db.add(flat)
        db.commit()
        db.refresh(flat)
        return flat
    else : raise HTTPException(status_code=status.HTTP_202_ACCEPTED, detail=f"Already rented")

def flat_assign_details(db:Session):
    flats=db.query(FlatAssignment).all()
    return flats

def get_details_byID(id:int , db:Session):
    flat=db.query(FlatAssignment).get(id)
    return flat


# def delete_assignment_by_id(id: int,db: Session):
#     ref = db.query(FlatAssignment).get(id)
#     if not ref:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Flat with id {id} not found")
#     else:
#         change_status(id, db)
#         db.delete(ref)
#     db.commit()

