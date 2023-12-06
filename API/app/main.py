# app/main.py
from fastapi import FastAPI
from app.api import main as api_main  # Import API routes from app/api

app = FastAPI()

app.include_router(api_main.router)  # Include the API routes
