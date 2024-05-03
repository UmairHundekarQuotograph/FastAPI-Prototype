from sqlalchemy.orm import Session

import models, schemas

def get_student(db: Session, name: str):
    return db.query(models.Student).filter(models.Student.firstname == name).first()

def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(firstname=student.firstname,
                                lastname = student.lastname,
                                age = student.age,
                                mark =student.mark)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def delete_student(db: Session, name: str):
    db_student = get_student(db=db, name=name)
    db.delete(db_student)
    db.commit()
    return {"Message": "Student deleted"}

def update_student_mark(db: Session, name: str, new_mark: float):
    db_student = get_student(db=db, name=name)
    setattr(db_student, 'mark', new_mark)
    db.commit()
    db.refresh(db_student)
    return db_student
