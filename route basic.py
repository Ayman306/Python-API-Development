from fastapi import FastAPI

app=FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to my web server!"}

@app.get("/posts")
def get_posts():
    return {"data": "This is your post!"}
