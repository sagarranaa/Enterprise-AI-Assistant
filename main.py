from fastapi import FastAPI

from app.api.routes import router


app = FastAPI(
    title="Enterprise AI Assistant"
)

app.include_router(router)