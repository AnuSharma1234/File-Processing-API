from app.models import File
from app.utils.filename import generate_storage_name

async def upload_file(
    file,
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
        original_name=file.filename,
        storage_name=storage_name,
        file_path=path,
        mime_type=file.content_type
    )

    db.add(db_file)

    await db.commit()

    await db.refresh(db_file)

    return db_file