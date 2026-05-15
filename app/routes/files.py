from fastapi import APIRouter, Depends , UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.dependencies import get_db
from app.models import File

from app.services.validation import validate_file
from app.services.storage import LocalStorageService
from app.services.file_service import upload_file

fileRouter = APIRouter()


@fileRouter.get("/files")
async def list_files(
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(File))

    files = result.scalars().all()

    return files

@fileRouter.post("/files")
async def create_file(
    file: UploadFile,
    db=Depends(get_db)
):
    await validate_file(file)

    storage=LocalStorageService()
    
    db_file=await upload_file(
        file,
        db,
        storage
    )

    return {
        "job_id":str(
            db_file.id
        ),
        "status":"pending"
    }