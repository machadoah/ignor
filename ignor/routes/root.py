from fastapi import APIRouter

from ignor.schemas import Message

router = APIRouter(
    prefix='/api',
    tags=['root'],
)


@router.get('/', response_model=Message)
async def root():
    """
    Root endpoint
    """
    return {'message': 'Hello World'}
