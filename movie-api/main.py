from fastapi import FastAPI, Body, Path, Query, Request, HTTPException, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from typing import Optional, List
from jwt_manager import create_token, validate_token
from fastapi.security import HTTPBearer

app = FastAPI()
app.title = "My fisrt app with FastAPI"
app.version = "0.0.1"

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data['email'] != "bernardo@gmail.com":
            raise HTTPException(status_code=403, detail="Invalid credentials")

class User(BaseModel):
    email: str
    password: str

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5, max_Length=30)
    year: int = Field(le=2023)
    director_name: str = Field(min_Length=5, max_Length=20)
    imdbRating: float = Field(gt=0, le=10)
    category: str = Field(min_length=1, max_length=10)

    model_config = {
        "json_schema_extra": {
            "example": {
                "id":1,
                "title":"a movie",
                "year": 2023,
                "director_name": "a director",
                "imdbRating": 5.0,
                "category": "cine"
            }
        }
    }

movies = [
    {
        "id": 1,
        "title":"The Shawshank",
        "year": 1994,
        "director_name": "Bernardo",
        "imdbRating":8.3,
        "category":"Action"
    },
    {
        "id": 2,
        "title":"Redemption",
        "year": 1994,
        "director_name": "Bernardo",
        "imdbRating":8.3,
        "category":"Comedy"
    }
]



@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello baby</h1>')



@app.post('/login', tags=['auth'])
def login(user: User):
    if user.email == "bernardo@gmail.com" and user.password == "bernard":
        token: str = create_token(user.dict())
        return JSONResponse(status_code=200, content=token)




@app.get('/movies', tags=['movies'], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    return JSONResponse(status_code=200, content=movies)





@app.get('/movies/{id}', tags=['movies'], response_model=Movie)
def get_movie(id: int= Path(ge=1, le=2000)) -> Movie:
    for item in movies:
        if item['id'] == id:
            return JSONResponse(content=item)
    return JSONResponse(status_code=404, content=[])

@app.get('/movies/', tags=['movies'], response_model=List[Movie])
def get_movies_by_category(category: str = Query(min_length=5, max_length=15)) -> List[Movie]:
    data = [item for item in movies if item["category"] == category]
    return JSONResponse(content=data)

@app.post('/movies', tags=['movies'], response_model=dict, status_code=201)
def create_movie(movie: Movie) -> dict:
    movies.append(movie)
    return JSONResponse(status_code=201, content={"message": "Your movie has been registered"})

@app.put('/movies/{id}',  tags=['movies'], response_model=dict, status_code=200)
def update_movie(id: int, movie: Movie) -> dict:
    for item in movies:
        if item["id"] == id:
            item['title'] = movie.title
            item['year'] = movie.year
            item['director_name'] = movie.director_name
            item['imdbRating'] = movie.imdbRating
            item['category'] = movie.category
    return JSONResponse(status_code=200, content={"message": "Your movie has been modified"})

@app.delete('/movies/{id}',  tags=['movies'], response_model=dict, status_code=200)
def delete_movie(id: int) -> dict:
    for item in movies:
        if item['id'] == id:
            movies.remove(item)
    return JSONResponse(status_code=200, content={"message": "Your movie has been deleted"})
