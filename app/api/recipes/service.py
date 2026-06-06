from typing import Sequence

from fastapi import HTTPException

from app.api.recipes.schemas import RecipeCreate
from app.core.models import Recipe, RecipeIngredientLink, RecipeTagLink
from app.core.repository import IngredientRepository, RecipeRepository, TagRepository


class RecipeService:
    def __init__(
        self,
        recipe_repo: RecipeRepository,
        ingredient_repo: IngredientRepository,
        tag_repo: TagRepository,
    ) -> None:
        self.recipe_repo = recipe_repo
        self.ingredient_repo = ingredient_repo
        self.tag_repo = tag_repo

    def list_recipes(self, offset: int = 0, limit: int = 20) -> Sequence[Recipe]:
        return self.recipe_repo.list(offset=offset, limit=limit)

    def get_recipe(self, recipe_id: int) -> Recipe:
        recipe = self.recipe_repo.get(recipe_id)
        if recipe is None:
            raise HTTPException(status_code=404, detail="Recipe not found")
        return recipe

    def create_recipe(self, data: RecipeCreate) -> Recipe:
        recipe = self.recipe_repo.add(
            Recipe(name=data.name, description=data.description)
        )
        self.recipe_repo.flush()  # populate recipe.id

        self._attach_ingredients(recipe, data)
        self._attach_tags(recipe, data)

        self.recipe_repo.commit()
        self.recipe_repo.refresh(recipe)
        return recipe

    def _attach_ingredients(self, recipe: Recipe, data: RecipeCreate) -> None:
        for item in data.ingredients:
            if not self.ingredient_repo.get(item.ingredient_id):
                raise HTTPException(
                    status_code=422,
                    detail=f"Ingredient {item.ingredient_id} not found",
                )
            self.recipe_repo.add(
                RecipeIngredientLink(
                    recipe_id=recipe.id,
                    ingredient_id=item.ingredient_id,
                    quantity=item.quantity,
                    unit=item.unit,
                )
            )

    def _attach_tags(self, recipe: Recipe, data: RecipeCreate) -> None:
        for tag_id in data.tag_ids:
            if not self.tag_repo.get(tag_id):
                raise HTTPException(
                    status_code=422,
                    detail=f"Tag {tag_id} not found",
                )
            self.recipe_repo.add(RecipeTagLink(recipe_id=recipe.id, tag_id=tag_id))
