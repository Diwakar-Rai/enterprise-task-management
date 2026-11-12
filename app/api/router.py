from fastapi import APIRouter 

router = APIRouter() 

@router.get("/health")
async def health_check():
    return {"status": "healthy", "message": "Enterprise Task Management API is running"}