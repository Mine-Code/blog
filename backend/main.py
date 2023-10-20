from fastapi import FastAPI
from db import db

from models.posts import Post

app = FastAPI()

@app.get("/api/test")
async def test():
  response = {
      "message": "hello world"
  }
  return response

@app.get("/api/posts")
async def get_posts():
  session = db.get_db()
  posts = session.query(Post).all()
  return posts
