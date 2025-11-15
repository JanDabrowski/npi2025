from fastapi import FastAPI, Form
from typing import Annotated
from .db import register_user, create_db_and_tables

app = FastAPI()


@app.on_event("startup")
def on_startup():
    # Ensure database tables exist when the application starts
    create_db_and_tables()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/register")
async def register(
    email: Annotated[str, Form()],
    password: Annotated[str, Form()],
):
    success = register_user(email, password)
    return {"success": success}
