from typing import TYPE_CHECKING, Optional

from sqlalchemy.types import Enum
from sqlmodel import Column, Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .ingredient import Ingredient
    from .recipe import Recipe
    from .tag import Tag

from app.core.utils import Unit


class RecipeTagLink(SQLModel, table=True):
    recipe_id: Optional[int] = Field(
        default=None, foreign_key="recipe.id", primary_key=True
    )
    tag_id: Optional[int] = Field(default=None, foreign_key="tag.id", primary_key=True)

    tag: "Tag" = Relationship(back_populates="recipes")
    recipe: "Recipe" = Relationship(back_populates="tags")


class RecipeIngredientLink(SQLModel, table=True):
    recipe_id: int = Field(foreign_key="recipe.id", primary_key=True)
    ingredient_id: int = Field(foreign_key="ingredient.id", primary_key=True)

    quantity: float
    unit: Unit = Field(sa_column=Column(Enum(Unit)))

    ingredient: "Ingredient" = Relationship(back_populates="recipes")
    recipe: "Recipe" = Relationship(back_populates="ingredients")
