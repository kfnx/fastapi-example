from typing import Optional

from dotenv import load_dotenv
from sqlmodel import Field, Session, SQLModel, create_engine

from app.config import settings

load_dotenv(override=True)
engine = create_engine(settings.database_url)


def get_db_session():
    with Session(engine) as session:
        yield session


class Note(SQLModel, table=True):
    id: int = Field(primary_key=True)
    title: str = Field(default="Untitled")
    content: Optional[str] = Field(default="")
