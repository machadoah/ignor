from fastapi import FastAPI

from ignor.routes.templates import templates_router

app = FastAPI(
    title="Ignor API",
    description="API for Ignor",
    version="0.1.0",
)

app.include_router(
    templates_router,
    tags=["templates"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/health")
async def health():
    return {"status": "healthy"}
