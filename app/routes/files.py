from fastapi import APIRouter, Depends , UploadFile , File
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.dependencies import get_db

from app.constants import FileStatus

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
    file: UploadFile = File(...),
    db=Depends(get_db)
):
    size = await validate_file(file)

    db_file=await upload_file(
        file=file,
        file_size=size,
        db=db,
        storage=LocalStorageService()
    )

    return {
        "job_id":str(
            db_file.id
        ),
        "status":FileStatus.PENDING
    }