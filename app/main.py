from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.routes import pronunciation, phrases, users

app = FastAPI(
    title="Language Learning API",
    description="API for Language Learning System with AI Integration",
    version="1.0.0"
)

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(users.router, prefix="/api/users", tags=["users"])
app.include_router(pronunciation.router, prefix="/api/pronunciation", tags=["pronunciation"])
app.include_router(phrases.router, prefix="/api/phrases", tags=["phrases"])

@app.get("/")
async def root():
    return {"message": "Welcome to Language Learning API"}
