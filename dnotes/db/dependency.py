from typing import Generator
from sqlalchemy.orm import sessionmaker , declarative_base
from sqlalchemy import create_engine, MetaData
from dnotes.settings import settings

engine = create_engine(settings.db_str)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db() -> Generator:
    db = Session()
    try:
        yield db
    finally:
        db.close()