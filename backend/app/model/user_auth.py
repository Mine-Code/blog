from sqlmodel import Field

from app.model.base_model import BaseSQLModel


class UserAuth(BaseSQLModel, table=True):
  __tablename__ = "user_auths"

  user_id: int = Field(foreign_key="users.id")
  identity_type: str = Field(max_length=255)
  identifier: str = Field(max_length=255)
  credential: str = Field(max_length=255)
