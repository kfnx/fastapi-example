from typing import Optional

from pydantic import BaseModel, field_validator


class NoteCreate(BaseModel):
    title: str
    content: str

    @field_validator("title")
    def validate_title(cls, v):
        if not v or v.strip() == "":
            raise ValueError("Title cannot be empty")
        return v.strip()

    @field_validator("content")
    def validate_content(cls, v):
        if not v or v.strip() == "":
            raise ValueError("Content cannot be empty")
        return v.strip()


class NoteRead(BaseModel):
    id: int
    title: str
    content: str


class NoteUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None


class NoteDelete(BaseModel):
    id: int
