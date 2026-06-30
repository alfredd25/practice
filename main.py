from fastapi import FastAPI, Path, Query, HTTPException

app = FastAPI()

notes = [{"id": 1, "name": "Zap"}, {"id": 2, "name": "Apple"}, {"id": 3, "name": "Banana"}]

@app.get("/")
def read():
  return {"hello" : "world"}

@app.post("/")
def write():
  notes.append("Hello")

  return {"message": "Item added", "current_list": notes}

@app.patch("/")
def update():
  new = int(input())
  notes[0] = new

  return {"message": "Updated successfully", "current_list": notes}

@app.delete("/")
def delete():
  notes.remove("hello")

  return {"message": "Deleted successfully", "current_list" : notes}

@app.get('/notes/{note_id}')
def read_note(note_id: str = Path(..., description="Id of the note in the db", example="N001, N002...")):
  if note_id in notes:
    return notes[note_id]
  else:
    return {"Error": "Note not found. Try a different id"}

@app.get('/sort')
def sort_notes(sort_by: str = Query(..., description="Sort notes in asc order based on name"), order_by: str = Query('asc')):
  if order_by not in ['asc', 'desc']:
    raise HTTPException(status_code = 400, detail = "Invalid order_by value. Must be 'asc' or 'desc'.")
  
  sort_order = True if order_by == 'desc' else False
  sorted_notes = sorted(notes,key=lambda x: x[sort_by],  reversed = sort_order)

  return sorted_notes

if __name__ == "__main__":
  import uvicorn

  uvicorn.run(app, host="0.0.0.0", port=8000)