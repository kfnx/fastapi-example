from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class NoteCreate(BaseModel):
    title: str
    content: str

class NoteRead(BaseModel):
    id: int
    title: str
    content: str

class NoteUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

class NoteDelete(BaseModel):
    id: int