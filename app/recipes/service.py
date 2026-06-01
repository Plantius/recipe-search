from sqlmodel import Session, select

from app.core.models import Recipe


class RecipeService:
    @staticmethod
    def list(session: Session):
        return session.exec(select(Recipe)).all()

    @staticmethod
    def create(session: Session, recipe: Recipe):
        session.add(recipe)
        session.commit()
        session.refresh(recipe)
        return recipe
