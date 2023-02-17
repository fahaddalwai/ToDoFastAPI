from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import settings

DATABASE_USERNAME = settings.database_username
DATABASE_SERVER = settings.database_server
DATABASE_PASSWORD = settings.database_password
DATABASE_HOSTNAME = settings.database_hostname
DATABASE_NAME = settings.database_name


SQLALCHEMY_DATABASE_URL = "sqlite:///./Todo.db"


engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db() -> any:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()