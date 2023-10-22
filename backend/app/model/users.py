import datetime

from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy import Column, Integer, String
from app.model.base_model import Base

class Users(Base):
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True)
  username = Column(String(40))
  email = Column(String(255))
  registered_on = Column(DateTime, default=datetime.datetime.utcnow)
  