from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from dnotes.db.dependency import Base
from sqlalchemy.orm import relationship

class Note(Base):
    __tablename__ = "Notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    owner_id = relationship("User", back_populates="notes")








