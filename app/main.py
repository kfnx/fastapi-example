from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

from app.routers import notes

app = FastAPI(
    title="hello FastAPI",
    description="A simple User API with FastAPI and Scalar integration",
)

app.include_router(notes.router)


@app.get("/")
def hello_world():
    """Hello world"""
    return {"hello": "fast-api world", "docs": "/scalar"}


@app.get("/health")
def health_check():
    """Health check endpoint for container orchestration"""
    return {"status": "healthy", "service": "fastapi-notes"}


@app.get("/scalar", include_in_schema=False)
async def scalar_html():
    """Scalar API documentation"""
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title,
    )
