from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlalchemy import Column, DateTime, func
from sqlmodel import Field, Relationship, SQLModel

from .links import RecipeTagLink

if TYPE_CHECKING:
    from .recipe import Recipe


class Tag(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(min_length=1, max_length=255, index=True, unique=True)

    recipes: list["Recipe"] = Relationship(
        back_populates="tags", link_model=RecipeTagLink
    )

    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(
        sa_column=Column(
            DateTime, default=func.now(), onupdate=func.now(), nullable=False
        )
    )
