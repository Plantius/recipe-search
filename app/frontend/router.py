import logging

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError

from app.api.recipes.dependencies import RecipeServiceDep
from app.api.recipes.schemas import RecipeRead
from app.api.tags.dependencies import TagServiceDep

logger = logging.getLogger(__name__)
router = APIRouter()
templates = Jinja2Templates(directory="app/frontend/templates")


@router.get("/", name="index", response_class=HTMLResponse)
async def index(request: Request, recipe_svc: RecipeServiceDep, tag_svc: TagServiceDep):
    recipes = recipe_svc.list_recipes()
    tags = tag_svc.list_tags()
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"recipes": recipes, "tags": tags},
    )


@router.get("/recipes", name="recipes_page", response_class=HTMLResponse)
async def recipes_page(request: Request, recipe_svc: RecipeServiceDep):
    recipes = recipe_svc.list_recipes()
    return templates.TemplateResponse(
        request=request,
        name="recipes.html",
        context={"recipes": recipes},
    )


@router.get("/recipes/{recipe_id}", name="recipe_detail", response_class=HTMLResponse)
async def recipe_detail(request: Request, recipe_id: int, recipe_svc: RecipeServiceDep):
    recipe = recipe_svc.get_recipe(recipe_id)
    try:
        recipe_read = RecipeRead.model_validate(recipe)
    except ValidationError as e:
        logger.error("Failed to validate recipe %d: %s", recipe_id, e)
        raise HTTPException(status_code=500, detail=str(e))
    return templates.TemplateResponse(
        request=request,
        name="recipe_detail.html",
        context={"recipe": recipe_read},
    )
