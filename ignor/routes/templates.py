from fastapi import APIRouter


templates_router = APIRouter(
    prefix="/api/v1/templates",
    tags=["templates"],
)
@templates_router.get("/")
async def get_templates():
    """
    Get all templates
    """
    return {"templates": ["template1", "template2", "template3"]}


