from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
from User.models import User
from User.schemas import SUserBase, SUserCreate, SUser
from SystemRole.models import SystemRole
from SystemRole.schemas import SSystemRole, SSystemRoleBase, SSystemRoleCreate
from database import engine, Base

app = FastAPI(
    title="SEMS"
)

@app.post("/roles")
async def create_role(role: SSystemRoleCreate) -> SSystemRole:
    db_role = await crud.get_system_role_by_name(system_role_name= role.role_name)
    if db_role:
        raise HTTPException(status_code=400, detail="Role already exist")
    return await crud.create_system_role(role=role)

@app.get("/roles/{role_id}")
async def get_role(role_id: int) -> SSystemRole: 
    return await crud.get_system_role(system_role_id=role_id)

@app.post("/users")
async def create_user(user: SUserCreate, system_role_id: int) -> SUser:
    db_role = await crud.get_system_role(system_role_id = system_role_id)
    if not db_role:
        raise HTTPException(status_code=400, detail="Role does not exist")
    db_user = await crud.get_user_by_email(email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already in use")
    
    return await crud.create_user(user=user, system_role_id=system_role_id)

