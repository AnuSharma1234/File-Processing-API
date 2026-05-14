from sqlalchemy import Column, Integer, String , Text , DateTime
from sqlalchemy.sql import func
from app.constants import FileStatus

from .db import Base

class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True)

    # Original uploaded filename
    filename = Column(String, nullable=False)

    # Stored file path in local storage/S3 later
    storage_path = Column(String, nullable=False)

    # File type
    file_type = Column(String, nullable=False)

    # File size in bytes
    file_size = Column(Integer, nullable=False)

    # Processing status
    # pending | processing | completed | failed
    status = Column(String, default=FileStatus.PENDING , nullable=False)

    # Extracted content
    extracted_text = Column(Text, nullable=True)

    # Error logs if processing fails
    error_message = Column(Text, nullable=True)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )