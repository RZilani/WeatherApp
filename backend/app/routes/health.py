from fastapi import APIRouter


router = APIRouter(
    prefix="/health",
    tags= ["Health"]
)

@router.get("/")
async def health_check():
    # TODO: Add actual health checks later:
    # - Database connection
    # - OpenWeatherMap API connectivity
    # - Memory usage, disk space, etc.
    
    return {
        "status": "healthy",
        "service": "weather-platform",
        "version": "1.0.0",
        "timestamp": "2024-01-01T12:00:00Z"  # We'll make this dynamic later
    }