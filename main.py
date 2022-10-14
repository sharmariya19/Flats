from fastapi import FastAPI,  status,Depends , HTTPException
from database import engine, Base , get_db
from Flats_fun import create_details,get_all_Flatdetails,get_detail_byID, update_detail_by_id,delete_detail_by_id
from typing import List
from sqlalchemy.orm import Session

from schemas import Flat_create, show_flat
app = FastAPI()
Base.metadata.create_all(engine)
@app.get("/")
def root():
    return "Gives the details of the flats"

@app.get("/flats",response_model=List[show_flat])
def read_all_flats(db:Session = Depends(get_db)):
    ref = get_all_Flatdetails(db=db)
    return ref

@app.post("/flats/",response_model=show_flat, status_code=status.HTTP_201_CREATED)
def create_job(detail: Flat_create,db: Session = Depends(get_db)):
    ref = create_details(obj=detail,db=db)
    return ref

@app.get("/flats/{id}",response_model=show_flat)
def read_flat(id:int,db:Session = Depends(get_db)):
    ref = get_detail_byID(id=id,db=db)
    if not ref:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Flat with this id {id} does not exist")
    return ref

@app.put("/flats/{id}")   
def update_flat(id: int,ref: Flat_create,db: Session = Depends(get_db)):
    update_detail_by_id(id=id,obj=ref,db=db)
    
    return {"msg":"Successfully updated data."}

@app.delete("/flats/{id}") 
def delete_job(id: int,db: Session = Depends(get_db)):
    delete_detail_by_id(id=id,db=db)
    
    return {"msg":"Successfully deleted."}
