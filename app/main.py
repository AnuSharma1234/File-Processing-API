from fastapi import FastAPI , Depends
from contextlib import asynccontextmanager
from .dependencies import get_db
from sqlalchemy.orm import Session
from app.routes.health import healthRouter
from app.routes.files import fileRouter
from .init_db import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()

    yield

    print("Closing server")


app = FastAPI(lifespan=lifespan)

app.include_router(healthRouter)
app.include_router(fileRouter)

@app.get('/')
def root(db: Session = Depends(get_db)):
    return {"message" : "DB Connected"}
