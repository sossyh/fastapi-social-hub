from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel
from random import randrange

class post(BaseModel):
    title: str
    content: str   
    published: bool = True
    rating: Optional[int] = None

app = FastAPI()

my_posts = []
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/posts")
def get_posts():
    return my_posts

@app.get("/posts/{post_id}")
def get_post(post_id: int):
    for post in my_posts:
        if post['id'] == post_id:
            return post
    return {"error": "Post not found"}

@app.post("/posts")
def create_posts(post: post):
    post_id = randrange(100)
    post_dict = post.model_dump()
    post_dict['id'] = post_id
    my_posts.append(post_dict)
    return post_dict
    