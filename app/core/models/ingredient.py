from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .links import RecipeIngredientLink


class Ingredient(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    name: str = Field(min_length=1, max_length=255, index=True, unique=True)
    recipes: list["RecipeIngredientLink"] = Relationship(back_populates="ingredient")

    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    # TODO: Extend with more details
