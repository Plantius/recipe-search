from fastapi import APIRouter, Request, Response

router = APIRouter()


@router.get("/", name="search")
async def search(request: Request):
    return {"status": "ok"}
