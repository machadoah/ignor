from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from ignor.routes import root, templates

app = FastAPI(
    title='Ignor API',
    description='API for Ignor',
    version='0.1.0',
)


@app.get('/')
async def redirect_to_docs():
    """
    Redirect to the docs
    """
    return RedirectResponse(url='/docs')


app.include_router(
    templates.router,
    tags=['templates'],
)

app.include_router(
    root.router,
    tags=['root'],
)
