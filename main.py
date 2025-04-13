from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None
   
@app.get("/")
def root():
    return {"message": "Hellogg World"}
 

@app.get("/posts") 
def get_posts():
    return {"Data": "Hello World posts"}


@app.post("/createposts")
def create_posts(new_post: Post):
    print(new_post.rating)
    return {"new_post": new_post}
