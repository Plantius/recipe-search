from pydantic import BaseModel, ConfigDict, Field

# --- Shared / nested ---


class IngredientRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    # id: int
    name: str


class TagRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    # id: int
    name: str


# --- Input schemas ---


class RecipeIngredientCreate(BaseModel):
    """What the client sends when adding an ingredient to a recipe."""

    ingredient_id: int
    quantity: float
    unit: str


class RecipeCreate(BaseModel):
    name: str
    description: str | None = None
    ingredients: list[RecipeIngredientCreate] = Field(default_factory=list)
    tag_ids: list[int] = Field(default_factory=list)


class RecipeTagRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    tag: TagRead


# --- Output schemas ---


class RecipeIngredientRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    ingredient: IngredientRead
    quantity: float
    unit: str


class RecipeRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    # id: int
    name: str
    description: str | None = None
    ingredients: list[RecipeIngredientRead] = Field(default_factory=list)
    tags: list[RecipeTagRead] = Field(default_factory=list)
