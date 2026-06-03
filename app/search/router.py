from fastapi import APIRouter, Request

router = APIRouter()


@router.get("/", name="search")
async def search(request: Request):
    return {"status": "ok"}
