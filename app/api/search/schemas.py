from pydantic import BaseModel, Field


class SearchQuery(BaseModel):
    query: str | None = None
    offset: int = Field(0, ge=0)
    limit: int = Field(20, ge=0)
    tags: list[str] = []
