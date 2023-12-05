from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func


class User:
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    user_name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())