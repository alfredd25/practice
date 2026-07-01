from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class NoteCreate(BaseModel):
  #Length constrains min 3 aan pinne max 50 chars.
  name: str = Field(..., #... means str field is MANDATORY
                    min_length = 3,
                    max_length = 50,
                    description="Name of the note",
                    examples=["Buy Groceries"]
  )

  is_important: bool = False #Also optional cause no '...' and with a default value
  
  description: Optional[str] = Field(None, max_length = 100) #Optional field can be None or missing no scene

  creator_email: EmailStr

class NoteResponse(BaseModel):
  id: int
  name: str
  is_important: bool
  description: Optional[str]
  creator_email: EmailStr