from app.models import File
from app.utils.filename import generate_storage_name
from app.constants import FileStatus

async def upload_file(
    file,
    file_size,
    db,
    storage
):

    storage_name=generate_storage_name(
        file.filename
    )

    path=await storage.save(
        file,
        storage_name
    )

    db_file=File(
        filename=file.filename,
        storage_name=storage_name,
        storage_path=path,
        file_type=file.content_type,
        file_size=file_size,
        status=FileStatus.PENDING
    )

    db.add(db_file)

    await db.commit()

    await db.refresh(db_file)

    return db_file