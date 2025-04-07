#CRUD
#C -> Create -> POST
#R -> Read   -> GET
#U -> Update -> PUT/PATCH
#D -> Delete -> DELETE

from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
app=FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts=[{"title": "100 days in desearted island", "content": "I am going to stay in this desearted island for 100 days", "id": 1},
            {"title": "100 days in goa", "content": "I am going to stay in goa for 100 days", "id": 2}]

def find_post(id):
    for p in my_posts:
        if p["id"]==id:
            return p

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p["id"]==id:
            return i
@app.get("/")
async def root():
    return {"message": "Welcome to my web server!"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create(post: Post):
    post_dict=post.dict()
    post_dict["id"]=randrange(0, 10000000)

    my_posts.append(post_dict)
    return {"Data": post_dict} 

#retrieving only one post

@app.get("/posts/{id}")
def get_post(id: int):
    post=find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"post with id: {id} was not found")
    return {"post details": post}
    
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = 0
    for post in my_posts:
        if post["id"]==id:
            my_posts.pop(index)
            return {"message": "post was deleted"}
        index += 1
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    detail=f"post with id: {id} was not found")

@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    index=find_index_post(id)

    if index==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"post with id: {id} was not found")

    post_dict=post.dict()
    post_dict["id"]=id
    my_posts[index]=post_dict
    return {"data": post_dict}


