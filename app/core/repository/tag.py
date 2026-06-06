from sqlmodel import Session

from app.core.models import Tag
from app.core.repository.base import BaseRepository


class TagRepository(BaseRepository[Tag]):
    model = Tag

    def __init__(self, session: Session) -> None:
        super().__init__(session)
