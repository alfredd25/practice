from pydantic import BaseModel

class NoteBase(BaseModel):
  name: str

class NoteResponse(NoteBase):
  id: int
  name: str