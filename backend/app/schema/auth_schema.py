from datetime import datetime

from pydantic import BaseModel

from app.schema.user_schema import User


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
        


class SignUp(BaseModel):
  identity_type: str
  identifier: str
  raw_credential: str
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


class Payload(BaseModel):
  id: int
  # uuid: str
  # username: str
  # is_superuser: bool


class SignInResponse(BaseModel):
  access_token: str
  expiration: datetime
  user_info: User
