from fastapi import APIRouter, Depends, status, HTTPException
from database import get_db
from sqlalchemy.orm import Session
from typing import List
from schemas.flat import show_flat, Flat_create
from crud_func.Flats_fun import create_details,get_all_Flatdetails, get_detail_byID, delete_detail_by_id, update_detail_by_id
from routers.login import oauth2_scheme
from jose import jwt

router = APIRouter()


@router.get("/flats",tags=['flat'],response_model=List[show_flat], status_code=status.HTTP_200_OK)
def read_all_flats(db:Session = Depends(get_db)):
    ref = get_all_Flatdetails(db=db)
    return ref

@router.post("/flats", tags=['flat'], response_model=show_flat, status_code=status.HTTP_201_CREATED)
def create_flat(detail: Flat_create,db: Session = Depends(get_db), token : str=Depends(oauth2_scheme)):
    ref = create_details(obj=detail,db=db)
    return ref

@router.get("/flats/{id}", tags=['flat'], response_model=show_flat, status_code=status.HTTP_200_OK)
def read_flat(id:int,db:Session = Depends(get_db)):
    ref = get_detail_byID(id=id,db=db)
    if not ref:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Flat with this id {id} does not exist")
    return ref

@router.put("/flats/{id}", tags=['flat'], status_code=status.HTTP_200_OK)   
def update_flat(id: int,ref: Flat_create,db: Session = Depends(get_db), token : str=Depends(oauth2_scheme)):
    update_detail_by_id(id=id,obj=ref,db=db)
    
    return {"msg":"Successfully updated data."}

@router.delete("/flats/{id}",  tags=['flat'], status_code=status.HTTP_200_OK) 
def delete_job(id: int,db: Session = Depends(get_db), token : str=Depends(oauth2_scheme)):
    delete_detail_by_id(id=id,db=db)
    
    return {"msg":"Successfully deleted."}
