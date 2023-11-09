from typing import List
from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from app.schema.base_schema import FindBase, ModelBaseInfo, SearchOptions
from app.schema.user_schema import BaseUser, User
from app.util.schema import AllOptional


class RawIdentifier(BaseModel):
  identity_type: str
  identifier: str
  raw_credential: str

  class Config:
    schema_extra = {
      "example": {
        "identity_type": "email",
        "identifier": "hoge@example.com",
        "raw_credential": "password"
      }
    }

class Identifier(BaseModel):
  identity_type: str
  identifier: str
  credential: str

  class Config:
    schema_extra = {
      "example": {
        "identity_type": "email",
        "identifier": "hoge@example.com",
        "credential": "$2a$12$WPsh1opaliluzH60./CyVurxjX/Vp4T5dnuGUcnmtwjO77bSUKR9W"
      }
    }


class SignIn(BaseModel):
  identity_type__eq: str
  identifier__eq: str
  raw_credential: str

  class Config:
    schema_extra = {
      "example": {
        "identity_type__eq": "email",
        "identifier__eq": "hoge@example.com",
        "raw_credential": "password"
      }
    }
        

class SignUp(RawIdentifier):
  username: str

  class Config:
    schema_extra = {
      "example": {
        "identity_type": "email",
        "identifier": "hoge@example.com",
        "raw_credential": "password",
        "username": "hoge"
      }
    }


class RegisterResponse(User):
  ...
  identifiers: List[Identifier]
  class Config:
    schema_extra = {
      "example": {
        "username": "hoge",
        "uuid": "1a2b3c4d5e6f7e8d",
        "is_active": True,
        "is_superuser": False,
        "created_at": "2006-01-02T15:04:05.000Z",
        "updated_at": "2006-01-02T15:04:05.000Z",
        "identifiers": [
          {
            "identity_type": "email",
            "identifier": "hoge@example.com",
            "credential": "$2a$12$WPsh1opaliluzH60./CyVurxjX/Vp4T5dnuGUcnmtwjO77bSUKR9W"
          }
        ]
      }
    }

class Payload(BaseModel):
  id: int
  # uuid: str
  # username: str
  # is_superuser: bool


class SignInResponse(BaseModel):
  access_token: str
  expiration: datetime
  user_info: User


class FindAuthByIdentifier(FindBase, metaclass=AllOptional):
  identity_type__eq: str
  identifier__eq: str
  ...

class FindAuthByUser(FindBase, metaclass=AllOptional):
  user_id__eq: int
  ...
