import logging
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError
from sqlmodel import Session

from app.core import service as core_service
from app.core.database import get_session
from app.recipes import service as recipe_service
from app.recipes.schemas import RecipeRead

SessionDep = Annotated[Session, Depends(get_session)]

logger = logging.getLogger(__name__)

router = APIRouter()

templates = Jinja2Templates(directory="app/frontend/templates")


@router.get("/", name="index", response_class=HTMLResponse)
async def index(request: Request, session: SessionDep):
    recipes = recipe_service.list_recipes(session)
    tags = core_service.list_tags(session)
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"recipes": recipes, "tags": tags},
    )


@router.get("/recipes/{recipe_id}", name="recipe_detail", response_class=HTMLResponse)
def recipe_detail(
    request: Request,
    recipe_id: int,
    session: Session = Depends(get_session),
):
    recipe = recipe_service.get_recipe(session, recipe_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    try:
        recipe_read = RecipeRead.model_validate(recipe)
    except ValidationError as e:
        logger.error("Failed to validate Recipe details:", e)

    return templates.TemplateResponse(
        request=request,
        name="recipe_detail.html",
        context={"recipe": recipe_read},
    )


@router.get("/recipes", name="recipes_page", response_class=HTMLResponse)
async def recipes_page(request: Request, session: SessionDep):
    recipes = recipe_service.list_recipes(session)
    # TODO: Fetch recipe details
    return templates.TemplateResponse(
        request=request,
        name="recipes.html",
        context={"recipes": recipes},
    )


@router.get("/search", name="search_page", response_class=HTMLResponse)
async def search_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="search.html",
        context={},
    )
