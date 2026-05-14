from fastapi import APIRouter , Depends , status
from fastapi.responses import JSONResponse
from sqlalchemy import text
from app.db import AsyncSessionLocal

healthRouter = APIRouter()

@healthRouter.get('/health')
def health_check():
    db = AsyncSessionLocal()

    try:
        db.execute(text("SELECT 1"))

        return {
            "status" : "healthy"
        }
    
    except Exception:
        return JSONResponse(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            content={
                "status" : "unhealthy"
            }
        )
    
    finally:
        db.close()
