from fastapi import FastAPI

from ignor.routes import root, templates

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
