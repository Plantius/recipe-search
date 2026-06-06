from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from app.api.tags.schemas import TagRead
from app.core.models.types import Unit


class IngredientRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str


class RecipeIngredientCreate(BaseModel):
    ingredient_id: int
    quantity: float
    unit: Unit


class RecipeCreate(BaseModel):
    name: str
    description: str | None = None
    ingredients: list[RecipeIngredientCreate] = Field(default_factory=list)
    tag_ids: list[int] = Field(default_factory=list)


class RecipeIngredientRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    ingredient: IngredientRead
    quantity: float
    unit: str


class RecipeRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    description: str | None = None
    instructions: list[str] = Field(default_factory=list)
    ingredients: list[RecipeIngredientRead] = Field(default_factory=list)
    tags: list[TagRead] = Field(default_factory=list)

    created_at: datetime
    updated_at: datetime
