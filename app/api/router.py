from fastapi import APIRouter

from app.search.router import router as search_router

api_router = APIRouter()


api_router.include_router(
    search_router,
    prefix="/search",
    tags=["search"],
)
