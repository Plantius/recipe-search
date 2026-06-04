from typing import Sequence

from sqlmodel import Session, select

from app.core.models import Tag


def list_tags(session: Session) -> Sequence[Tag]:
    statement = select(Tag)
    return session.exec(statement).all()
