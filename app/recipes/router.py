from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.core.database import get_session
from app.core.models import Recipe
from app.recipes.schemas import RecipeCreate, RecipeRead
from app.recipes.service import RecipeService

router = APIRouter()


@router.get("/", response_model=list[RecipeRead])
def list_recipes(session: Session = Depends(get_session)):
    return RecipeService.list(session)


@router.post("/create", response_model=RecipeRead)
def create_recipe(
    payload: RecipeCreate,
    session: Session = Depends(get_session),
):
    recipe = Recipe.model_validate(payload)
    return RecipeService.create(session, recipe)
