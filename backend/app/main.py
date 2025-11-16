from fastapi import FastAPI, Form
from typing import Annotated
from .db import register_user, create_db_and_tables, login_user
app = FastAPI()


@app.on_event("startup")
def on_startup():
    # Ensure database tables exist when the application starts
    create_db_and_tables()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/create-user")
async def register(
    email: Annotated[str, Form()],
):
    success = register_user(email)
    return {"success": success}

@app.get("/login")
async def login_user(
    email: Annotated[str, Form()],
    password: Annotated[str, Form()],
):
    success = login_user(email, password)
    return {"success": success}