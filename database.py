from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://yyojaouz:ShUEL3DLf2fceu6OJHcXc-vkyORVAAfq@cornelius.db.elephantsql.com/yyojaouz"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

Base = declarative_base()