from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlalchemy import JSON, Column, DateTime, func
from sqlmodel import Field, Relationship, SQLModel

from .links import RecipeTagLink

if TYPE_CHECKING:
    from .links import RecipeIngredientLink
    from .tag import Tag


class Recipe(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(min_length=1, max_length=255, index=True)
    description: Optional[str] = None
    instructions: list[str] = Field(default_factory=list, sa_column=Column(JSON))

    tags: list["Tag"] = Relationship(back_populates="recipes", link_model=RecipeTagLink)
    ingredients: list["RecipeIngredientLink"] = Relationship(back_populates="recipe")

    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(
        sa_column=Column(
            DateTime, default=func.now(), onupdate=func.now(), nullable=False
        )
    )
