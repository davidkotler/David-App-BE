from typing import Generator
from sqlalchemy.orm import sessionmaker , declarative_base
from sqlalchemy import create_engine, MetaData
from dnotes.settings import settings

engine = create_engine(settings.db_str) #need to add real DBgt
Session = sessionmaker(bind=engine)

Base = declarative_base()

Base.metadata.create_all(bind=engine)


def get_db() -> Generator:
    db = Session()
    try:
        yield db
    finally:
        db.close()