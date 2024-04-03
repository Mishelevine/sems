from pydantic import BaseModel

class UserBase(BaseModel):
    first_name: str
    last_name: str
    paternity: str
    email: str

class UserCreate(UserBase):
    hashed_password: str
    pass

class User(UserBase):
    id: int
    system_role_id: int

    class Config:
        orm_mode = True

class SystemRoleBase(BaseModel):
    role_name: str

class SystemRoleCreate(SystemRoleBase):
    pass

class SystemRole(SystemRoleBase):
    id: int

    class Config:
        orm_mode = True