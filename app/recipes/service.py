from typing import Sequence

from fastapi import HTTPException
from sqlalchemy.orm import selectinload
from sqlmodel import Session, select

from app.core.models import Ingredient, Recipe, RecipeIngredientLink, RecipeTagLink, Tag
from app.recipes.schemas import RecipeCreate


def list_recipes(session: Session) -> Sequence[Recipe]:
    statement = select(Recipe).options(
        selectinload(Recipe.ingredients).selectinload(RecipeIngredientLink.ingredient),
        selectinload(Recipe.tags),
    )
    return session.exec(statement).all()


def get_recipe(session: Session, recipe_id: int) -> Recipe | None:
    statement = (
        select(Recipe)
        .where(Recipe.id == recipe_id)
        .options(
            selectinload(Recipe.ingredients).selectinload(
                RecipeIngredientLink.ingredient
            ),
            selectinload(Recipe.tags),
        )
    )
    return session.exec(statement).one_or_none()


def get_recipes(session: Session, recipe_ids: list[int]) -> Sequence[Recipe]:
    statement = (
        select(Recipe)
        .where(Recipe.id in recipe_ids)
        .options(
            selectinload(Recipe.ingredients).selectinload(
                RecipeIngredientLink.ingredient
            ),
            selectinload(Recipe.tags),
        )
    )
    return session.exec(statement).all()


def create_recipe(session: Session, data: RecipeCreate) -> Recipe:
    recipe = Recipe(name=data.name, description=data.description)
    session.add(recipe)
    session.flush()

    for item in data.ingredients:
        ingredient = session.get(Ingredient, item.ingredient_id)
        if not ingredient:
            raise HTTPException(
                status_code=422, detail=f"Ingredient {item.ingredient_id} not found"
            )
        session.add(
            RecipeIngredientLink(
                recipe_id=recipe.id,
                ingredient_id=item.ingredient_id,
                quantity=item.quantity,
                unit=item.unit,
            )
        )

    for tag_id in data.tag_ids:
        if not session.get(Tag, tag_id):
            raise HTTPException(status_code=422, detail=f"Tag {tag_id} not found")
        session.add(RecipeTagLink(recipe_id=recipe.id, tag_id=tag_id))

    session.commit()
    session.refresh(recipe)
    return recipe
