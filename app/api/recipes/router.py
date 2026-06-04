from fastapi import APIRouter

import app.api.recipes.service as service
from app.api.recipes.schemas import RecipeCreate, RecipeRead
from app.core.database import SessionDep

router = APIRouter()


@router.get("/", response_model=list[RecipeRead])
def list_recipes(session: SessionDep, offset: int = 0, limit: int = 20):
    return service.list_recipes(session, offset, limit)


@router.get("/{recipe_id}", name="api_recipe_detail", response_model=RecipeRead)
def recipe_detail(recipe_id: int, session: SessionDep):
    return service.get_recipe(session, recipe_id)


@router.post("/", response_model=RecipeRead, status_code=201)
def create_recipe(payload: RecipeCreate, session: SessionDep):
    return service.create_recipe(session, payload)
