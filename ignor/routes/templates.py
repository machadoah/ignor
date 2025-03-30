from fastapi import APIRouter

router = APIRouter(
    prefix='/api/templates',
    tags=['templates'],
)


@router.get('/')
async def get_templates():
    """
    Get all templates
    """
    return {'templates': ['template1', 'template2', 'template3']}
