# main.py
from fastapi import FastAPI, Path, Query, HTTPException
from schema import NoteCreate, NoteResponse  

app = FastAPI()

notes = [
    {"id": 1, "name": "Zap"}, 
    {"id": 2, "name": "Apple"}, 
    {"id": 3, "name": "Banana"}
]

@app.get("/")
def read():
    return {"hello": "world"}

@app.post("/notes", response_model=NoteResponse)
def write(note_input: NoteCreate):
    new_id = len(notes) + 1

    new_note = {"id": new_id, "name": note_input.name}
    notes.append(new_note)

    return new_note

@app.patch("/notes/{note_id}", response_model=NoteResponse)
def update_note(note_id: int, note_input: NoteCreate):
    for note in notes:
        if note["id"] == note_id:
            note["name"] = note_input.name
            return note
            
    raise HTTPException(status_code=404, detail="Note not found")

@app.get('/notes/{note_id}', response_model=NoteResponse)
def read_note(note_id: int = Path(..., description="Id of the note in the db")):
    for note in notes:
        if note["id"] == note_id:
            return note
    raise HTTPException(status_code=404, detail="Note not found.")

@app.get('/sort')
def sort_notes(sort_by: str = Query('name', description="Sort notes based on name"), order_by: str = Query('asc')):
    if order_by not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail="Invalid order_by value. Must be 'asc' or 'desc'.")
    
    is_reversed = True if order_by == 'desc' else False
    
    try:
        sorted_notes = sorted(notes, key=lambda x: x[sort_by], reverse=is_reversed)
        return sorted_notes
    except KeyError:
        raise HTTPException(status_code=400, detail=f"Cannot sort by invalid field: {sort_by}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)