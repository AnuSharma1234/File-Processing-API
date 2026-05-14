import asyncio

from app.db import engine, Base

from app.models import File

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


asyncio.run(init_db())