from fastapi import FastAPI, Query

from src.client.router import router as client_router

app = FastAPI()

app.include_router(client_router)
