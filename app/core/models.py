from typing import Optional

from sqlmodel import Field, Relationship, SQLModel

from app.core.utils import Unit


class RecipeTagLink(SQLModel, table=True):
    recipe_id: Optional[int] = Field(
        default=None, foreign_key="recipe.id", primary_key=True
    )
    tag_id: Optional[int] = Field(default=None, foreign_key="tag.id", primary_key=True)


class RecipeIngredientLink(SQLModel, table=True):
    recipe_id: int = Field(foreign_key="recipe.id", primary_key=True)
    ingredient_id: int = Field(foreign_key="ingredient.id", primary_key=True)

    quantity: float
    unit: Unit


class Ingredient(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    name: str = Field(index=True, unique=True)
    # TODO: Extend with more details


class Tag(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    name: str = Field(index=True, unique=True)
    recipes: Optional[list["Recipe"]] = Relationship(
        back_populates="tags", link_model=RecipeTagLink
    )


class Recipe(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    name: str = Field(index=True)
    description: Optional[str] = None

    tags: Optional[list[Tag]] = Relationship(
        back_populates="recipes", link_model=RecipeTagLink
    )

    ingredients: list["Ingredient"] = Relationship(
        back_populates="recipes", link_model=RecipeIngredientLink
    )
