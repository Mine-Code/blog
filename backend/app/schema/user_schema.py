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
    schema_extra = {
      "example": {
        "username": "new-username",
        "is_active": True,
        "is_superuser": False,
      }
    }
  

# class BaseUserWithAuths(BaseUser):
#   auths: List[str] = []

#   class Config:
#     orm_mode = True

class User(ModelBaseInfo, BaseUser, metaclass=AllOptional):
  ...


class FindUserAuth(FindBase, BaseUser, metaclass=AllOptional):
  identity_type__eq: str
  identifier__eq: str
  ...


class UpsertUser(BaseUser, metaclass=AllOptional):
  ...

class FindUserResult(BaseModel):
  founds: Optional[List[User]]
  search_options: Optional[SearchOptions]
