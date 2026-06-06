from typing import Annotated

from fastapi import Depends

from app.api.recipes.service import RecipeService
from app.core.database import SessionDep
from app.core.repository import IngredientRepository, RecipeRepository, TagRepository


def get_recipe_repo(session: SessionDep) -> RecipeRepository:
    return RecipeRepository(session)


def get_ingredient_repo(session: SessionDep) -> IngredientRepository:
    return IngredientRepository(session)


def get_tag_repo(session: SessionDep) -> TagRepository:
    return TagRepository(session)


RecipeRepoDep = Annotated[RecipeRepository, Depends(get_recipe_repo)]
IngredientRepoDep = Annotated[IngredientRepository, Depends(get_ingredient_repo)]
TagRepoDep = Annotated[TagRepository, Depends(get_tag_repo)]


def get_recipe_service(
    recipe_repo: RecipeRepoDep,
    ingredient_repo: IngredientRepoDep,
    tag_repo: TagRepoDep,
) -> RecipeService:
    return RecipeService(
        recipe_repo=recipe_repo,
        ingredient_repo=ingredient_repo,
        tag_repo=tag_repo,
    )


RecipeServiceDep = Annotated[RecipeService, Depends(get_recipe_service)]
