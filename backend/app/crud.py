from sqlalchemy.orm import Session
from . import models

def get_students(db: Session):
    return db.query(models.Student).all()

def create_student(db: Session, name: str):
    new_student = models.Student(name=name)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student
