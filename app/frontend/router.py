from typing import Annotated

from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session

from app.core.database import get_session
from app.recipes import service as recipe_service

SessionDep = Annotated[Session, Depends(get_session)]

router = APIRouter()

templates = Jinja2Templates(directory="app/frontend/templates")


@router.get("/", response_class=HTMLResponse)
async def index(request: Request, session: SessionDep):
    recipes = recipe_service.list_recipes(session)
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"recipes": recipes},
    )


@router.get("/search", response_class=HTMLResponse)
async def search_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="search.html",
        context={},
    )
