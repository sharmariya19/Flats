from schemas import Flat_create
from sqlalchemy.orm import Session
from models import Flats
from fastapi import HTTPException,status
def create_details(obj:Flat_create,db: Session ):
    flat_ref=Flats(**obj.dict())
    db.add(flat_ref)
    db.commit()
    db.refresh(flat_ref)
    return flat_ref

def get_all_Flatdetails(db:Session):
    obj=db.query(Flats).all()
    return obj

def get_detail_byID(id:int , db:Session):
    obj=db.query(Flats).get(id)
    return obj

def update_detail_by_id(id:int, obj: Flat_create,db: Session):
    ref = db.query(Flats).get(id)
    if not ref:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Flat with id {id} not found")
    else:
        ref.status=obj.status
        ref.rooms=obj.rooms
        ref.halls=obj.halls
        ref.monthly_rent=obj.monthly_rent
        ref.sqft_area=obj.sqft_area
        ref.floor_no=obj.floor_no

    db.commit()


def delete_detail_by_id(id: int,db: Session):
    ref = db.query(Flats).get(id)
    if not ref:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Flat with id {id} not found")
    else:
        db.delete(ref)
    db.commit()
    
