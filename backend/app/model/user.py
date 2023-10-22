from sqlmodel import Field

from app.model.base_model import BaseSQLModel


class User(BaseSQLModel, table=True):
  __tablename__ = "users"

  username: str = Field(max_length=40, nullable=False, unique=True)
