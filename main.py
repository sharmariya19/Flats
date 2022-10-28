from fastapi import FastAPI
from config import setting
from database import engine, Base
from routers import users, flats, flat_assign, login

tags_metadata = [{
    "name":"user",
    "description":"details about user"
    },
    {
        "name":"flat",
        "description":"details about flat"
    },
    {
        "name":"flatassign",
        "description":"details about flat assignment"
    }
]


app = FastAPI(title = setting.TITLE, openapi_tags=tags_metadata)
Base.metadata.create_all(bind = engine)

app.include_router(users.router)
app.include_router(login.router)
app.include_router(flats.router)
app.include_router(flat_assign.router)

