from typing import Annotated

from fastapi import Depends

from app.api.tags.service import TagService
from app.core.database import SessionDep
from app.core.repository import TagRepository


def get_tag_repo(session: SessionDep) -> TagRepository:
    return TagRepository(session)


def get_tag_service(
    tag_repo: Annotated[TagRepository, Depends(get_tag_repo)],
) -> TagService:
    return TagService(tag_repo=tag_repo)


TagServiceDep = Annotated[TagService, Depends(get_tag_service)]
