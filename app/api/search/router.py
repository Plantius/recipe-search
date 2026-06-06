from typing import Annotated

from fastapi import APIRouter, Query

from app.api.recipes.schemas import RecipeRead
from app.api.search.dependencies import SearchServiceDep
from app.api.search.schemas import SearchQuery

router = APIRouter()


@router.get("/", name="api_search", response_model=list[RecipeRead])
def search_recipes(service: SearchServiceDep, params: Annotated[SearchQuery, Query()]):
    return service.search_recipes(params)
