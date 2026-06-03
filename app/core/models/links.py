from typing import TYPE_CHECKING

from sqlalchemy.types import Enum
from sqlmodel import Column, Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .ingredient import Ingredient
    from .recipe import Recipe

from app.core.models.types import Unit


class RecipeTagLink(SQLModel, table=True):
    recipe_id: int = Field(foreign_key="recipe.id", primary_key=True)
    tag_id: int = Field(foreign_key="tag.id", primary_key=True)


class RecipeIngredientLink(SQLModel, table=True):
    recipe_id: int = Field(foreign_key="recipe.id", primary_key=True)
    ingredient_id: int = Field(foreign_key="ingredient.id", primary_key=True)
    quantity: float
    unit: Unit = Field(sa_column=Column(Enum(Unit), nullable=False))
    ingredient: "Ingredient" = Relationship(back_populates="recipes")
    recipe: "Recipe" = Relationship(back_populates="ingredients")
