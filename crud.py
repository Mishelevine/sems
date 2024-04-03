from sqlalchemy import insert, select
from database import async_session_maker
import passlib.hash

from User.models import User
from User.schemas import SUserBase, SUserCreate, SUser
from SystemRole.models import SystemRole
from SystemRole.schemas import SSystemRole, SSystemRoleBase, SSystemRoleCreate


async def get_user(user_id: int):
    async with async_session_maker() as session:
        query = select(User).filter(User.id == user_id)
        result = await session.execute(query)
        return result.scalar_one_or_none()

async def get_user_by_email(email: str):
    async with async_session_maker() as session:
        query = select(User).filter(User.email == email)
        result = await session.execute(query)
        return result.scalar_one_or_none()

async def create_user(user: SUserCreate, system_role_id:int):
    async with async_session_maker() as session:
        db_user = User(email=user.email, 
                        system_role_id=system_role_id, 
                        hashed_password = passlib.hash.bcrypt.hash(user.hashed_password),
                        first_name = user.first_name,
                        last_name = user.last_name,
                        paternity = user.paternity)
        session.add(db_user)
        await session.commit()
        await session.refresh(db_user)
        return db_user

async def get_system_role(system_role_id: int):
    async with async_session_maker() as session:
        query = select(SystemRole).filter(SystemRole.id == system_role_id)
        result = await session.execute(query)
        return result.scalar_one_or_none()

async def get_system_role_by_name(system_role_name: str):
    async with async_session_maker() as session:
        query = select(SystemRole).filter(SystemRole.role_name == system_role_name)
        result = await session.execute(query)
        return result.scalar_one_or_none()

async def create_system_role(role: SSystemRoleCreate):
    async with async_session_maker() as session:
        db_role = SystemRole(role_name = role.role_name)
        session.add(db_role)
        await session.commit()
        await session.refresh(db_role)
        return db_role