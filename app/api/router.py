from fastapi import APIRouter

from app.recipes.router import router as recipes_router
from app.search.router import router as search_router

api_router = APIRouter()

api_router.include_router(
    recipes_router,
    prefix="/recipes",
    tags=["recipes"],
)

api_router.include_router(
    search_router,
    prefix="/search",
    tags=["search"],
)
