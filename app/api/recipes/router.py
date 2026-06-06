from fastapi import APIRouter

from app.api.recipes.dependencies import RecipeServiceDep
from app.api.recipes.schemas import RecipeCreate, RecipeRead

router = APIRouter()


@router.get("/", name="api_list_recipes", response_model=list[RecipeRead])
def list_recipes(service: RecipeServiceDep, offset: int = 0, limit: int = 20):
    return service.list_recipes(offset, limit)


@router.get("/{recipe_id}", name="api_recipe_detail", response_model=RecipeRead)
def recipe_detail(recipe_id: int, service: RecipeServiceDep):
    return service.get_recipe(recipe_id)


@router.post("/", response_model=RecipeRead, status_code=201)
def create_recipe(payload: RecipeCreate, service: RecipeServiceDep):
    return service.create_recipe(payload)
