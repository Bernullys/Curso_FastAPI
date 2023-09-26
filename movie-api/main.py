from fastapi import FastAPI
from fastapi.responses import HTMLResponse

movies = [
    {
        "id": 1,
        "title":"The Shawshank Redemption",
        "year": 1994,
        "director_name": "Bernardo",
        "imdbRating":8.3,
        "genre":"Action"
    },
    {
        "id": 2,
        "title":"The Shawshank Redemption",
        "year": 1994,
        "director_name": "Bernardo",
        "imdbRating":8.3,
        "genre":"Action"
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
