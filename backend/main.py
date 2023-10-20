from fastapi import FastAPI

app = FastAPI()

@app.get("/api/test")
async def test():
  response = {
      "message": "hello world"
  }
  return response
