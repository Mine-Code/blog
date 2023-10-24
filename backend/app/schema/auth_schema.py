from datetime import datetime

from pydantic import BaseModel

from app.schema.user_schema import User


class SignIn(BaseModel):
  identity_type__eq: str
  identifier__eq: str
  credential: str


class SignUp(BaseModel):
  identity_type: str
  identifier: str
  raw_credential: str
  username: str


class Payload(BaseModel):
  id: int
  identity_type: str
  identifier: str
  username: str
  # is_superuser: bool


class SignInResponse(BaseModel):
  access_token: str
  expiration: datetime
  user_info: User
