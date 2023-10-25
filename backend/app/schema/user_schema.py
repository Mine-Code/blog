from typing import List, Optional

from pydantic import BaseModel

from app.schema.base_schema import FindBase, ModelBaseInfo, SearchOptions
from app.util.schema import AllOptional

class BaseUser(BaseModel):
  username: str
  uuid: str
  is_active: bool
  is_superuser: bool

  class Config:
    orm_mode = True
  

# class BaseUserWithAuths(BaseUser):
#   auths: List[str] = []

#   class Config:
#     orm_mode = True

class User(ModelBaseInfo, BaseUser, metaclass=AllOptional):
  ...
  class Config:
    schema_extra = {
      "example": {
        "username": "hoge",
        "uuid": "1a2b3c4d5e6f7e8d",
        "is_active": True,
        "is_superuser": False,
        "created_at": "2006-01-02T15:04:05.000Z",
        "updated_at": "2006-01-02T15:04:05.000Z",
      }
    }


class FindUserAuth(FindBase, BaseUser, metaclass=AllOptional):
  identity_type__eq: str
  identifier__eq: str
  ...


class UpsertUser(BaseUser, metaclass=AllOptional):
  ...

class FindUserResult(BaseModel):
  founds: Optional[List[User]]
  search_options: Optional[SearchOptions]
