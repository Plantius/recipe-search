from sqlmodel import Session

from app.core.models import Ingredient
from app.core.repository.base import BaseRepository


class IngredientRepository(BaseRepository[Ingredient]):
    model = Ingredient

    def __init__(self, session: Session) -> None:
        super().__init__(session)
