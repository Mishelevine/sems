from pydantic import BaseModel

class UserBase(BaseModel):
    first_name: str
    last_name: str
    paternity: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    role_id: int

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

class UserDataBase(BaseModel):
    login: str
    email: str

class UserDataCreate(UserDataBase):
    password: str
    
class UserData(UserDataBase):
    user_id: int
    
    class Config:
        orm_mode = True