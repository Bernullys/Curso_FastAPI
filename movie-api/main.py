from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from fastapi.encoders import jsonable_encoder

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
def create_movie(id: int = Body(), title: str = Body(), year: int = Body(), director_name: str = Body(), imdbRating: float = Body(), category: str = Body()):
    movies.append(
        {
            'id': id,
            'title': title,
            'year': year,
            'director_name': director_name,
            'imdbRating': imdbRating,
            'category': category,
        }
    )
    return movies

@app.put('/movies/{id}',  tags=['movies'])
def update_movie(id: int, title: str = Body(), year: int = Body(), director_name: str = Body(), imdbRating: float = Body(), category: str = Body()):
    for item in movies:
        if item["id"] == id:
            item['title'] = title,
            item['year'] = year,
            item['director_name'] = director_name,
            item['imdbRating'] = imdbRating,
            item['category'] = category,
    return movies

@app.delete('/movies/{id}',  tags=['movies'])
def delete_movie(id: int):
    for item in movies:
        if item['id'] == id:
            movies.remove(item)
    return movies
