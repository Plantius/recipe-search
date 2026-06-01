from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.router import api_router
from app.core.database import init_db
from app.frontend.router import router as frontend_router
from app.recipes.router import router as recipes_router

app = FastAPI(
    title="Recipe Search",
)

init_db()

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static",
)

app.include_router(api_router, prefix="/api")
app.include_router(recipes_router, prefix="/recipes")
app.include_router(frontend_router)


@app.get("/health")
async def health():
    return {"status": "ok"}
