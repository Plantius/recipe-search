from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .links import RecipeIngredientLink, RecipeTagLink


class Recipe(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    name: str = Field(min_length=1, max_length=255, index=True)
    description: Optional[str] = None

    tags: Optional[list["RecipeTagLink"]] = Relationship(back_populates="recipe")

    ingredients: list["RecipeIngredientLink"] = Relationship(back_populates="recipe")

    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
