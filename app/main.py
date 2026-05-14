from fastapi import FastAPI , Depends
from .dependencies import get_db
from sqlalchemy.orm import Session
from app.routes.health import healthRouter

app = FastAPI()

app.include_router(healthRouter)

@app.get('/')
def root(db: Session = Depends(get_db)):
    return {"message" : "DB Connected"}

