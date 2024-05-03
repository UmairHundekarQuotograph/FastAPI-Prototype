from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
import models, schemas
from database import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.post("/create_student/", response_model=schemas.Student)
async def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    db_student = models.Student(firstname=student.firstname,
                                lastname = student.lastname,
                                age = student.age,
                                mark =student.mark)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


@router.get("/get_student", response_model=schemas.Student)
async def get_student(name: str, db: Session = Depends(get_db)):
    return db.query(models.Student).filter(models.Student.firstname == name).first()


@router.delete("/delete_student")
async def delete_student(name: str, db: Session = Depends(get_db)):
    db_student = get_student(db=db, name=name)
    db.delete(db_student)
    db.commit()
    return {"Message": "Student deleted"}

@router.put("/update_mark")
async def update_student(name: str, mark: float, db: Session = Depends(get_db)):
    db_student = get_student(db=db, name=name)
    setattr(db_student, 'mark', mark)
    db.commit()
    db.refresh(db_student)
    return db_student
