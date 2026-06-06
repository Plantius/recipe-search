from typing import Generic, Optional, Sequence, Type, TypeVar

from sqlmodel import Session, SQLModel, select

ModelT = TypeVar("ModelT", bound=SQLModel)


class BaseRepository(Generic[ModelT]):
    """
    Generic repository with common CRUD primitives.
    Subclasses override or extend as needed.
    """

    model: Type[ModelT]

    def __init__(self, session: Session) -> None:
        self.session = session

    def get(self, id: int) -> Optional[ModelT]:
        return self.session.get(self.model, id)

    def get_many(self, ids: list[int]) -> Sequence[ModelT]:
        return self.session.exec(
            select(self.model).where(
                self.model.id.in_(ids)  # ty:ignore[unresolved-attribute]
            )
        ).all()

    def list(self, offset: int = 0, limit: int = 20) -> Sequence[ModelT]:
        return self.session.exec(select(self.model).offset(offset).limit(limit)).all()

    def add(self, instance: ModelT) -> ModelT:
        self.session.add(instance)
        return instance

    def delete(self, instance: ModelT) -> None:
        self.session.delete(instance)

    def flush(self) -> None:
        self.session.flush()

    def commit(self) -> None:
        self.session.commit()

    def refresh(self, instance: ModelT) -> None:
        self.session.refresh(instance)
