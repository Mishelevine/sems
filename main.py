from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine, Base

app = FastAPI(
    title="SEMS"
)

Base.metadata.create_all(bind = engine)

async def get_db():
    async_db = SessionLocal()
    try:
        yield async_db
    finally:
        await async_db.close()

@app.post("/roles/", response_model=schemas.SystemRole)
async def create_role(role: schemas.SystemRoleCreate, db:Session = Depends(get_db)):
    db_role = await crud.get_system_role(db, role.role_name)
    if db_role:
        raise HTTPException(status_code=400, detail="Role already existed")
    return await crud.create_system_role(db=db, role=role)

# @app.get("/roles/{role_id}", response_model=schemas.SystemRole)
# def get_role(role: schemas.SystemRole, db: Session):
#     db_role = crud.get_system_role(db, system_role_id=role.role_id)
#     return(db_role)

# @app.post("/users/", response_model=schemas.User)
# async def create_user(user: schemas.UserCreate, system_role_name: str, db: Session = Depends(get_db)):
#     db_role = await crud.get_system_role(db=db, system_role_name = system_role_name)
#     if not db_role:
#         raise HTTPException(status_code=400, detail="Role does not exist")
#     db_user = await crud.get_user_by_email(db=db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already in use")
    
#     return await crud.create_user(db=db, user=user, system_role_id=db_role.id)

# @app.get("/users/{user_id}", response_model=schemas.User)
# async def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = await crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user