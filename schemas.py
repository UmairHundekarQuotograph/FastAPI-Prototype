from lib2to3.pytree import Base
from pydantic import BaseModel

class StudentBase(BaseModel):
    firstname: str
    lastname: str
    age: int
    mark: float

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    class Config:
        orm_mode = True

