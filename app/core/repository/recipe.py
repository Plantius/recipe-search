from typing import Optional, Sequence

from sqlalchemy.orm import selectinload
from sqlmodel import Session, select

from app.core.models import Recipe, RecipeIngredientLink, Tag
from app.core.repository.base import BaseRepository


class RecipeRepository(BaseRepository[Recipe]):
    model = Recipe

    def __init__(self, session: Session) -> None:
        super().__init__(session)

    def _eager_query(self):
        """Base query that always loads ingredients + tags in one round-trip."""
        return select(Recipe).options(
            selectinload(Recipe.ingredients).selectinload(
                RecipeIngredientLink.ingredient
            ),
            selectinload(Recipe.tags),
        )

    def list(self, offset: int = 0, limit: int = 20) -> Sequence[Recipe]:
        return self.session.exec(self._eager_query().offset(offset).limit(limit)).all()

    def get(self, recipe_id: int) -> Optional[Recipe]:
        return self.session.exec(
            self._eager_query().where(Recipe.id == recipe_id)
        ).one_or_none()

    def get_many(self, recipe_ids: list[int]) -> Sequence[Recipe]:
        return self.session.exec(
            self._eager_query().where(Recipe.id.in_(recipe_ids))
        ).all()

    def search(
        self,
        query: str | None = None,
        tags: list[str] | None = None,
        offset: int = 0,
        limit: int = 20,
    ) -> Sequence[Recipe]:
        stmt = self._eager_query()
        if query:
            stmt = stmt.where(Recipe.name.ilike(f"%{query}%"))

        if tags:
            for tag in tags:
                stmt = stmt.where(Recipe.tags.any(Tag.name == tag))

        stmt = stmt.distinct()

        return self.session.exec(stmt.offset(offset).limit(limit)).all()
