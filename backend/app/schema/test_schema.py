from pydantic import BaseModel

class TestResponse(BaseModel):
  message: str
  class Config:
    schema_extra = {
      "example": {
        "message": "test"
      }
    }
