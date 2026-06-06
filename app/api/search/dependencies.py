from typing import Annotated

from fastapi import Depends

from app.api.search.service import SearchService
from app.core.database import SessionDep
from app.core.repository import RecipeRepository


def get_recipe_repo(session: SessionDep) -> RecipeRepository:
    return RecipeRepository(session)


RecipeRepoDep = Annotated[RecipeRepository, Depends(get_recipe_repo)]


def get_search_service(
    recipe_repo: RecipeRepoDep,
) -> SearchService:
    return SearchService(recipe_repo=recipe_repo)


SearchServiceDep = Annotated[
    SearchService,
    Depends(get_search_service),
]
