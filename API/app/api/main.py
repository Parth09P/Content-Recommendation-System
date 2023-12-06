# app/api/main.py
from fastapi import APIRouter
from app.recommendation import movie

router = APIRouter()

@router.get("/")
@router.get("/home")
def read_root():
    print('Inside main')
    return {"message": "Hello, FastAPI API!"}

@router.get("/api/recommendation/{movie_name}")
def get_movies(movie_name):
    print('Inside second')
    movies = movie.movie_recommendation(movie_name)
    print(movies)
    return {"message": movies}
