from sqlalchemy import create_engine, MetaData
from dependency import Base, engine


def init_db():
    Base.metadata.create_all(bind=engine)


init_db()