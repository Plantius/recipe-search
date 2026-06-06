from typing import Annotated

from fastapi import APIRouter, Query, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.api.search.dependencies import SearchServiceDep
from app.api.search.schemas import SearchQuery
from app.api.tags.dependencies import TagServiceDep

router = APIRouter()
templates = Jinja2Templates(directory="app/frontend/templates")


@router.get("/", name="api_search", response_class=HTMLResponse)
def search_recipes(
    request: Request,
    service: SearchServiceDep,
    tag_svc: TagServiceDep,
    params: Annotated[SearchQuery, Query()],
):
    recipes = service.search_recipes(params)

    context = {
        "request": request,
        "recipes": recipes,
        "query": params.query,
        "selected_tags": params.tags,
        "tags": tag_svc.list_tags(),
    }

    if request.headers.get("HX-Request"):
        return templates.TemplateResponse(
            request=request, name="partials/_results.html", context=context
        )

    return templates.TemplateResponse(
        request=request, name="find_recipes.html", context=context
    )
