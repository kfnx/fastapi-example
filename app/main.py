from typing import List

from fastapi import Depends, FastAPI, HTTPException
from scalar_fastapi import get_scalar_api_reference
from sqlmodel import Session, select

from app.database import Note, get_db_session
from app.schema import NoteCreate, NoteRead, NoteUpdate

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
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@app.put("/notes/{note_id}", response_model=NoteRead)
def update_note(note_id: int, note_update: NoteUpdate, db: Session = Depends(get_db_session)):
    """Update a note by ID"""
    note = db.get(Note, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    
    if note_update.title is not None:
        note.title = note_update.title
    if note_update.content is not None:
        note.content = note_update.content
    
    db.add(note)
    db.commit()
    db.refresh(note)
    return note


@app.delete("/notes/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db_session)):
    """Delete a note by ID"""
    note = db.get(Note, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    
    db.delete(note)
    db.commit()
    return {"message": "Note deleted successfully"}


@app.get("/scalar", include_in_schema=False)
async def scalar_html():
    """Scalar API documentation"""
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title,
    )
