from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
app=FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to my web server!"}

@app.get("/posts")
def get_posts():
    return {"data": "This is your post!"}


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.post("/createpost")
def create(post: Post):

    print("Pydantic schema: ", post)
    print("Python Dictionary: ", post.dict())
    print("Ratings: ", post.rating)

    return {"Data": f"{post.dict()}"} 

#title, content, catogory....