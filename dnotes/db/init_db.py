from sqlalchemy import create_engine, MetaData
from dnotes.db.dependency import Base,engine


def init_db():
    Base.metadata.create_all(bind=engine)


init_db()