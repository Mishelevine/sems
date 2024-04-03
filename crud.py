from sqlalchemy.orm import Session
import passlib.hash

import models, schemas

async def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

async def create_user(db: Session, user: schemas.UserCreate, system_role_id: int):
    db_user = models.User(email=user.email, 
                          system_role_id=system_role_id, 
                          hashed_password = passlib.hash.bcrypt.hash(user.hashed_password),
                          first_name = user.first_name,
                          last_name = user.last_name,
                          paternity = user.paternity)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

async def get_system_role(db: Session, system_role_name: str):
    return db.query(models.SystemRole).filter(models.SystemRole.role_name == system_role_name).first()

async def create_system_role(db: Session, role: schemas.SystemRoleCreate):
    db_role = await get_system_role(db, role.role_name)
    if db_role:
        return db_role
    
    db_item = models.SystemRole(**role.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

async def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()