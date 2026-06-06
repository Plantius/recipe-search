from typing import Sequence

from app.core.models import Tag
from app.core.repository import TagRepository


class TagService:
    def __init__(self, tag_repo: TagRepository) -> None:
        self.tag_repo = tag_repo

    def list_tags(self) -> Sequence[Tag]:
        return self.tag_repo.list()
