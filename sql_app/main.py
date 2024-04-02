from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

app = FastAPI(
    title="SEMS"
)

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/roles/", response_model=schemas.SystemRole)
def create_role(role: schemas.SystemRoleCreate, db:Session = Depends(get_db)):
    db_role = crud.get_system_role(db, role.role_name)
    if db_role:
        raise HTTPException(status_code=400, detail="Role already existed")
    return crud.create_system_role(db=db, role=role)

# @app.get("/roles/{role_id}", response_model=schemas.SystemRole)
# def get_role(role: schemas.SystemRole, db: Session):
#     db_role = crud.get_system_role(db, system_role_id=role.role_id)
#     return(db_role)

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_role = crud.get_system_role(db=db, system_role_name=user.role_name)
    if not db_role:
        raise HTTPException(status_code=400, detail="Role does not exist")
    return crud.create_user(db=db, user=user, role_id=db_role.id)

# @app.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user