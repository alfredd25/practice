from fastapi import FastAPI

app = FastAPI()

notes = []

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
def read_note(note_id: str):
  return notes[note_id]


if __name__ == "__main__":
  import uvicorn

  uvicorn.run(app, host="0.0.0.0", port=8000)