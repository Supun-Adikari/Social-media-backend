from typing import Optional
from fastapi import FastAPI, Response, status,HTTPException
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


def find_index_post(id):
    for i,p in enumerate(my_post):
        if p['id'] == id:
            return i
        

@app.get("/")
def root():
    return {"message": "Hellogg World"}
 

@app.get("/posts") 
def get_posts():
    print(my_post)
    return {"Data": my_post}


@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_post.append(post_dict)
    print(my_post)
    return {"new_post": post_dict}


@app.get("/posts/{id}")
def get_post(id: int):
    for p in my_post:
        if p['id'] == id:
            return {"post_detail": p}
    

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} was not found")
   

@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index_post(id)

    if(index == None):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} does not exist")

    
    my_post.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

