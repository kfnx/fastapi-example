from typing import List

from fastapi import Depends, FastAPI
from scalar_fastapi import get_scalar_api_reference
from sqlmodel import Session, select

from app.database import Note, get_db_session
from app.schema import NoteCreate, NoteRead

app = FastAPI(
    title="hello FastAPI",
    description="A simple User API with FastAPI and Scalar integration",
)


@app.get("/notes", response_model=List[NoteRead])
def get_notes(db: Session = Depends(get_db_session)):
    """Get all notes"""
    return db.exec(select(Note)).all()


@app.post("/notes", response_model=NoteRead)
def create_note(note: NoteCreate, db: Session = Depends(get_db_session)):
    """Create a new note"""
    new_note = Note(title=note.title, content=note.content)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note


@app.get("/notes/{note_id}", response_model=NoteRead)
def get_note(note_id: int, db: Session = Depends(get_db_session)):
    """Get a note by ID"""
    note = db.get(Note, note_id)
    return note


@app.get("/scalar", include_in_schema=False)
async def scalar_html():
    """Scalar API documentation"""
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title,
    )