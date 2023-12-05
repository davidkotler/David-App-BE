from typing import Generator
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dnotes.settings import settings

engine = create_engine(settings.db_str) #need to add real db
Session = sessionmaker(bind=engine)


def get_db() -> Generator:
    db = Session()
    try:
        yield db
    finally:
        db.close()