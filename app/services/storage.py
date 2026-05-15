import aiofiles
import os
from abc import ABC, abstractmethod

UPLOAD_DIR="uploads"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)

class StorageService(ABC):

    @abstractmethod
    async def save(
        self,
        file,
        filename
    ):
        pass

class LocalStorageService(StorageService):

    async def save(
        self,
        file,
        filename
    ):
        path=f"{UPLOAD_DIR}/{filename}"

        async with aiofiles.open(
            path,
            "wb"
        ) as out:
            
            while chunk:= await file.read(1024):

                await out.write(chunk)

        await file.seek(0)

        return path