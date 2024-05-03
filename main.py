from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.post("/create_student/", response_model=schemas.Student)
async def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db=db, student=student)


@app.get("/get_student", response_model=schemas.Student)
async def get_student(name: str, db: Session = Depends(get_db)):
    return crud.get_student(name=name, db=db)

@app.delete("/delete_student")
async def delete_student(name: str, db: Session = Depends(get_db)):
    return crud.delete_student(db=db, name=name)

@app.put("/update_mark")
async def update_student(name: str, mark: float, db: Session = Depends(get_db)):
    return crud.update_student_mark(db=db, name=name, new_mark=mark)
