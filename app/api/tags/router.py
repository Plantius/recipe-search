from typing import Annotated

from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.api.tags import service
from app.api.tags.schemas import TagRead
from app.core.database import get_session

SessionDep = Annotated[Session, Depends(get_session)]
router = APIRouter()


@router.get("/", response_model=list[TagRead])
def list_tags(session: SessionDep):
    return service.list_tags(session)
