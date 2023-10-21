from pydantic import BaseModel

class BaseUser(BaseModel):
  message: str
