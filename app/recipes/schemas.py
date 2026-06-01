from typing import Optional

from sqlmodel import SQLModel

from app.core.models import Ingredient, Tag


class RecipeCreate(SQLModel):
    name: str
    description: Optional[str] = None
    tags: Optional[list[Tag]] = None
    ingredients: list[Ingredient]


class RecipeRead(SQLModel):
    id: int
    name: str
    description: Optional[str] = None
    tags: Optional[list[Tag]] = None
    ingredients: list[Ingredient]
