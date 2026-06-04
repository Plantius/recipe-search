from fastapi import APIRouter

from app.api.recipes.router import router as recipes_router
from app.api.search.router import router as search_router
from app.api.tags.router import router as tags_router

api_router = APIRouter()

api_router.include_router(recipes_router, prefix="/recipes", tags=["recipes"])

api_router.include_router(search_router, prefix="/search", tags=["search"])

api_router.include_router(tags_router, prefix="/tags", tags=["tags"])
