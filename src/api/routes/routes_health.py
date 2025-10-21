from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.db.session import SessionLocal
from sqlalchemy import text

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/health", tags=["health"])
def health_check(db: Session = Depends(get_db)):
    """
    Health check endpoint that validates DB connectivity and returns a simple payload.
    """

    try:
        #simple query
        db.execute(text("SELECT 1"))
        return {"status" : "ok", "db" : "connected"}
    except Exception as e:
        return{
            "status" : "error",
            "db" : "disconnected",
            "detail" : str(e)
        }