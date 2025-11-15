from __future__ import annotations

from typing import Optional

from sqlmodel import (
    create_engine,
    SQLModel,
    Session,
    Field,
    select,
)
from sqlalchemy import Column
from sqlalchemy import JSON as SA_JSON
from .security import hash_password
from fastapi import HTTPException, status
from app import config

# Engine should live at module scope so it is NOT treated as a model field.
engine = create_engine(config.DATABASE_CONNECTION_STRING)


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: Optional[int] = Field(default=None, primary_key=True)
    email: str
    password_hash: str
    extra: dict = Field(sa_column=Column(SA_JSON), default_factory=dict)


def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine, expire_on_commit=False) as session:
        yield session


def register_user(email: str, password: str, *, name: str | None = None, lastname: str | None = None, group: str | None = None, permissions: list | None = None) -> bool:
    with Session(engine) as session:
        email = email.lower()
        existing = session.exec(select(User).where(User.email == email)).first()
        if existing is not None:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="User with this email already exists",
            )

        if not email or not password:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email and password are required",
            )

        hashed_password = hash_password(password)
        user = User(email=email, password_hash=hashed_password)
        session.add(user)
        session.commit()
        return True

