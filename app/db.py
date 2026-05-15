import os
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker,
)

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_async_engine(
    DATABASE_URL,
    echo=True,
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# Declarative base is located in app.base to avoid creating engines when
# importing models (helps Alembic autogenerate run without triggering async IO).
from app.base import Base

# alembic commands after each model changes
# docker compose exec backend alembic revision --autogenerate -m "message"
# after this apply migrations
# docker compose exec backend alembic upgrade head


# command to get into postgres
# docker exec -it postgres-db psql -U postgres
# \c file_processing
# \dt