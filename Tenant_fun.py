from unicodedata import name
from schemas import tenant
from sqlalchemy.orm import Session
from models import Tenants
from fastapi import HTTPException,status


def new_tenant(obj:tenant,db: Session ):
    new_tenant= Tenants(**obj.dict())
    db.add(new_tenant)
    db.commit()
    db.refresh(new_tenant)
    return new_tenant

def get_all_Tenants(db:Session):
    tenants=db.query(Tenants).all()
    return tenants

def get_tenant_byID(id:int , db:Session):
    tenant=db.query(Tenants).get(id)
    return tenant

def update_tenant_by_id(id:int, obj: tenant,db: Session):
    ref = db.query(Tenants).get(id)
    if not ref:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Tenant with id {id} not found")
    else:
        ref.tenant_name = obj.tenant_name
        ref.company_name = obj.company_name
        ref.contact = obj.contact
        ref.address = obj.address
    db.commit()
    db.refresh(ref)


def delete_tenant_by_id(id: int,db: Session):
    ref = db.query(Tenants).get(id)
    if not ref:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Tenant with id {id} not found")
    else:
        db.delete(ref)
    db.commit()
    
