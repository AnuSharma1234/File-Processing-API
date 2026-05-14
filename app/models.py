from sqlalchemy import Column, Integer, String
from .db import Base

class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    status = Column(String)