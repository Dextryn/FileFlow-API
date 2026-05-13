from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from FileFlowAPI.app.routes import health, files

app = FastAPI(title="FileFlowAPI")

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Allows ALL HTTP methods (GET, POST, etc.)
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(files.router)
