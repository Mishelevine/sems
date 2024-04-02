from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class SystemRole(Base):
    __tablename__ = "system_roles"

    id = Column(Integer, primary_key=True)
    role_name = Column(String(50), nullable=False)
    
    users = relationship("User", back_populates="system_role")
    
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=None)
    paternity = Column(String(50), nullable=True)
    system_role_id = Column(Integer, ForeignKey('system_roles.id'))
    
    system_role = relationship("SystemRole", back_populates="users")

class UserData(Base):
    __tablename__ = "users_data"
    
    email = Column(String, primary_key=True)
    login = Column(String(52), nullable=False, unique=True)
    password = Column(String(20), nullable= False)
    user_id = Column(Integer, ForeignKey('users.id'))