from typing import Optional

from sqlalchemy.types import Enum
from sqlmodel import Column, Field, Relationship, SQLModel

from app.core.utils import Unit


class RecipeTagLink(SQLModel, table=True):
    recipe_id: Optional[int] = Field(
        default=None, foreign_key="recipe.id", primary_key=True
    )
    tag_id: Optional[int] = Field(default=None, foreign_key="tag.id", primary_key=True)

    tag: "Tag" = Relationship()
    recipe: "Recipe" = Relationship()


class RecipeIngredientLink(SQLModel, table=True):
    recipe_id: int = Field(foreign_key="recipe.id", primary_key=True)
    ingredient_id: int = Field(foreign_key="ingredient.id", primary_key=True)

    quantity: float
    unit: Unit = Field(sa_column=Column(Enum(Unit)))

    ingredient: "Ingredient" = Relationship()
    recipe: "Recipe" = Relationship()


class Ingredient(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    name: str = Field(index=True, unique=True)
    recipes: list[RecipeIngredientLink] = Relationship(back_populates="ingredient")
    # TODO: Extend with more details


class Tag(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    name: str = Field(index=True, unique=True)
    recipes: Optional[list["RecipeTagLink"]] = Relationship(back_populates="tag")


class Recipe(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    name: str = Field(index=True)
    description: Optional[str] = None

    tags: Optional[list[RecipeTagLink]] = Relationship(back_populates="recipe")

    ingredients: list["RecipeIngredientLink"] = Relationship(back_populates="recipe")
