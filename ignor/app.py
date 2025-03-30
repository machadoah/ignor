from fastapi import FastAPI

from ignor.routes import root, templates
from ignor.schemas import Message

app = FastAPI(
    title='Ignor API',
    description='API for Ignor',
    version='0.1.0',
)

app.include_router(
    templates.router,
    tags=['templates'],
)

app.include_router(
    root.router,
    tags=['root'],
)


@app.get('/', response_model=Message)
async def root():
    return {'message': 'Developed by @machadoah 🤓'}
