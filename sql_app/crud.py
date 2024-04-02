from sqlalchemy.orm import Session

from . import models, schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_user(db: Session, user: schemas.UserCreate, role_id: int):
    db_item = models.User(**user.dict(), system_role_id=role_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_system_role(db: Session, system_role_id: int):
    return db.query(models.SystemRole).filter(models.SystemRole.id == system_role_id).first()

def create_system_role(db: Session, role: schemas.SystemRoleCreate):
    db_item = models.SystemRole(**role.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item