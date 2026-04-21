from fastapi import APIRouter

router = APIRouter(prefix="/api")


@router.get("/test")
def test():
    return {"status": "API working fine ✅"}
