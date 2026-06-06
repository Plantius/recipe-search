from typing import Sequence

from app.api.search.schemas import SearchQuery
from app.core.models import Recipe
from app.core.repository import RecipeRepository


class SearchService:
    def __init__(self, recipe_repo: RecipeRepository) -> None:
        self.recipe_repo = recipe_repo

    def search_recipes(self, params: SearchQuery) -> Sequence[Recipe]:
        query = params.query.strip() if params.query and params.query.strip() else None
        return self.recipe_repo.search(
            query=query,
            tags=params.tags,
            offset=params.offset,
            limit=params.limit,
        )
