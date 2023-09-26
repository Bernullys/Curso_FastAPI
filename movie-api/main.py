from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import Optional

class Movie(BaseModel):
    id: Optional[int] = None
    title: str
    year: int
    director_name: str
    imdbRating: float
    category: str

movies = [
    {
        "id": 1,
        "title":"The Shawshank Redemption",
        "year": 1994,
        "director_name": "Bernardo",
        "imdbRating":8.3,
        "category":"Action"
    },
    {
        "id": 2,
        "title":"The Shawshank Redemption",
        "year": 1994,
        "director_name": "Bernardo",
        "imdbRating":8.3,
        "category":"Comedy"
    }
]

app = FastAPI()
app.title = "My fisrt app with FastAPI"
app.version = "0.0.1"

@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello baby</h1>')


@app.get('/movies', tags=['movies'])
def get_movies():
    return movies

@app.get('/movies/{id}', tags=['movies'])
def get_movie(id: int):
    for item in movies:
        if item['id'] == id:
            return item
    return []

@app.get('movies/', tags=['movies'])
def get_movies_by_category(category: str, year: int):
    return [item for item in movies if item['category'] == category]

@app.post('/movies', tags=['movies'])
def create_movie(movie: Movie):
    movies.append(movie)
    return movies

@app.put('/movies/{id}',  tags=['movies'])
def update_movie(id: int, movie: Movie):
    for item in movies:
        if item["id"] == id:
            item['title'] = movie.title
            item['year'] = movie.year
            item['director_name'] = movie.director_name
            item['imdbRating'] = movie.imdbRating
            item['category'] = movie.category
    return movies

@app.delete('/movies/{id}',  tags=['movies'])
def delete_movie(id: int):
    for item in movies:
        if item['id'] == id:
            movies.remove(item)
    return movies
