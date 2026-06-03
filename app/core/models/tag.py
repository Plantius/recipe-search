from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .links import RecipeTagLink


class Tag(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    name: str = Field(min_length=1, max_length=255, index=True, unique=True)
    recipes: Optional[list["RecipeTagLink"]] = Relationship(back_populates="tag")
