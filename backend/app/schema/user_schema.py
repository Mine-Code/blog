from pydantic import BaseModel

from app.schema.base_schema import FindBase, ModelBaseInfo, SearchOptions
from app.util.schema import AllOptional

class BaseUser(BaseModel):
  username: str
  email: str
  registered_on: str

  class Config:
    orm_mode = True

class User(ModelBaseInfo, BaseUser, metaclass=AllOptional):
  ...