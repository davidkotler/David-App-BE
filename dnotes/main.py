from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dnotes.api.routers.note_router import router
from auth.routers.auth_router import router as auth_router
import uvicorn
from dnotes.db import init_db
from settings import settings

app = FastAPI()

init_db.init_db()  # initialize db


# Add CORS middleware to allow all origins and methods
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000',"http://localhost:3000/notes"],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(router, prefix="/notes")
app.include_router(auth_router, prefix="/auth")

if __name__ == "__main__":
    if settings.env == "dev":
        uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
