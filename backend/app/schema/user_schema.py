from typing import List, Optional

from pydantic import BaseModel

from app.schema.base_schema import FindBase, ModelBaseInfo, SearchOptions
from app.util.schema import AllOptional

class BaseUser(BaseModel):
  username: str

  class Config:
    orm_mode = True
  

# class BaseUserWithAuths(BaseUser):
#   auths: List[str] = []

#   class Config:
#     orm_mode = True

class User(ModelBaseInfo, BaseUser, metaclass=AllOptional):
  ...


class FindUser(FindBase, BaseUser, metaclass=AllOptional):
  identity_type__eq: str
  identifier: str
  ...


class UpsertUser(BaseUser, metaclass=AllOptional):
  ...

class FindUserResult(BaseModel):
  founds: Optional[List[User]]
  search_options: Optional[SearchOptions]
