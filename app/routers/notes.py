from fastapi import APIRouter , Path, Query, HTTPException, status
from app.schemas.schema import NoteCreate, NoteResponse  

router = APIRouter(prefix ="/notes", tags = ["Notes"])

notes = [
    {"id": 1, "name": "Zap"}, 
    {"id": 2, "name": "Apple"}, 
    {"id": 3, "name": "Banana"}
]

@router.get("/", response_model=NoteResponse)
def read_all_notes():
    return notes

@router.post("/", response_model=NoteResponse)
def write_note(note_input: NoteCreate):
    new_id = len(notes) + 1

    new_note = {"id": new_id, "name": note_input.name}
    notes.append(new_note)

    return new_note

@router.get('/{note_id}', response_model = NoteResponse)
def read_note(note_id: int = Path(..., description="Id of the note in the db")):
    for note in notes:
        if note["id"] == note_id:
            return note
        else:
            raise HTTPException(status_code = 404, detail="Note not found")
        
