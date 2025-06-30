import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))


from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from . import models, crud, database

# Create tables
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Allow CORS (safe even with proxy)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/students")
def get_students(db: Session = Depends(get_db)):
    return crud.get_students(db)


@app.get("/")
def root():
    return {"message": "Student API is running"}



@app.post("/students")
def add_student(data: dict, db: Session = Depends(get_db)):
    if "name" not in data:
        raise HTTPException(status_code=400, detail="Name is required")
    return crud.create_student(db, data["name"])
