from typing import Optional

from sqlmodel import SQLModel

from app.core.models import RecipeIngredientLink, RecipeTagLink


class RecipeCreate(SQLModel):
    name: str
    description: Optional[str] = None
    tags: Optional[list[RecipeTagLink]] = None
    ingredients: list[RecipeIngredientLink]


class RecipeRead(SQLModel):
    id: int
    name: str
    description: Optional[str] = None
    tags: Optional[list[RecipeTagLink]] = None
    ingredients: list[RecipeIngredientLink]
