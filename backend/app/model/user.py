from sqlmodel import Field

from app.model.base_model import BaseSQLModel


class User(BaseSQLModel, table=True):
  __tablename__ = "users"

  username: str = Field(max_length=40, nullable=False, unique=True)
  uuid: str = Field(max_length=255, unique=True)
  is_active: bool = Field(default=True)
  is_superuser: bool = Field(default=False)
