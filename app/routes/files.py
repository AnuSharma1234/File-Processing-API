from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.dependencies import get_db
from app.models import File

fileRouter = APIRouter()


@fileRouter.get("/files")
async def list_files(
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(File))

    files = result.scalars().all()

    return files