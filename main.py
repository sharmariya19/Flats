from fastapi import FastAPI,  status,Depends , HTTPException
# from Tenant_fun import get_all_Tenants
from database import engine, Base , get_db
from Flats_fun import create_details,get_all_Flatdetails,get_detail_byID, update_detail_by_id,delete_detail_by_id,update_status_by_id
from typing import List
from sqlalchemy.orm import Session
from Users_fun import create_new_user
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer
from schemas import Flat_create, flat_assigned, show_flat , ShowUser , UserCreate, flat_assign
from login_fun import authenticate_user , create_access_token
# from Tenant_fun import new_tenant, get_all_Tenants, get_tenant_byID,update_tenant_by_id,delete_tenant_by_id 
from FlatAssignment_fun import flatassign, flat_assign_details, get_details_byID 
from schemas import Token
from datetime import timedelta

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

@app.post("/",response_model = ShowUser)
def create_user(user : UserCreate,db: Session = Depends(get_db)):
    user = create_new_user(user=user,db=db)
    return user 


@app.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),db: Session= Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password,db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}




@app.get("/flatassign",response_model=List[flat_assigned])
def flatassign_details(db:Session = Depends(get_db)):
    details = flat_assign_details(db=db)
    return details

@app.post("/flatassign",response_model=flat_assigned, status_code=status.HTTP_201_CREATED)
def flatassign_details(detail: flat_assign,db: Session = Depends(get_db)):
    details = flatassign(obj=detail,db=db)
    return details



@app.get("/flatassign/{id}",response_model=flat_assigned)
def flatassign_detail(id:int,db:Session = Depends(get_db)):
    detail = get_details_byID(id=id,db=db)
    if not detail:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Details with this id {id} does not exist")
    return detail

