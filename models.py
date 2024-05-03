from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from database import Base

class Student(Base):
    __tablename__ = "students"

    firstname = Column(String, index=True, primary_key=True)
    lastname = Column(String, index=True)
    age = Column(Integer)
    mark = Column(Float)