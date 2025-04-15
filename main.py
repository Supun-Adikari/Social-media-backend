from typing import Optional
from fastapi import FastAPI, Response, status
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_post = [{"title": "title of post 1", "content": "content of post 1", "id": 1},{"title": "title of post 2", "content": "content of post 2", "id": 2}]
   
@app.get("/")
def root():
    return {"message": "Hellogg World"}
 

@app.get("/posts") 
def get_posts():
    return {"Data": my_post}


@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_post.append(post_dict)
    return {"new_post": post_dict}


@app.get("/posts/{id}")
def get_post(id: int,response: Response):
    for p in my_post:
        if p['id'] == id:
            return {"post_detail": p}
    
    response.status_code = status.HTTP_404_NOT_FOUND
    return {"message": f"Post with {id} was not found"}