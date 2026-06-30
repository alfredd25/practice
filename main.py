from fastapi import FastAPI
from routers.notes import router as notes_router

app = FastAPI(Title = " My Organised FastAPI app")

@app.get("/")
def home():
  return {"message": " Welcome to my API. Go to /docs to see the endpoints"}

app.include_router(notes_router)

if __name__ == "__main__":
  import uvicorn
  uvicorn.run("main:app", host = "0.0.0.0", port = 8000, reload = True)