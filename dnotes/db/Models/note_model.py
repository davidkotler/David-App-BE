from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func


class Note:
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())








