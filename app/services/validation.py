import os
from fastapi import UploadFile , HTTPException

ALLOWED_EXTENSIONS = {
    ".pdf",
    ".txt",
    ".csv"
}

ALLOWED_MIME_TYPES = {
    "application/pdf",
    "text/plain",
    "text/csv"
}

MAX_FILE_SIZE = 10 * 1024 * 1024

async def validate_file(file : UploadFile):
    
    extension = os.path.splitext(
        file.filename
    )[1].lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Unsupported extension"
        )
    
    if file.content_type not in ALLOWED_MIME_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Invalid mime type"
        )
    
    content = await file.read()

    if len(content)==0:
        raise HTTPException(
            status_code=400,
            detail="Empty file"
        )
    
    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail="File too large"
        )
    
    await file.seek(0)