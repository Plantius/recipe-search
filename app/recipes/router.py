from typing import Annotated

from fastapi import APIRouter, Depends
from sqlmodel import Session

import app.recipes.service as service
from app.core.database import get_session
from app.recipes.schemas import RecipeCreate, RecipeRead

SessionDep = Annotated[Session, Depends(get_session)]

router = APIRouter()


@router.get("/", name="recipes", response_model=list[RecipeRead])
def list_recipes(session: SessionDep):
    return service.list_recipes(session)


@router.post("/", response_model=RecipeRead, status_code=201)
def create_recipe(payload: RecipeCreate, session: SessionDep):
    return service.create_recipe(session, payload)
