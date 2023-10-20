import datetime

from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy import Column, Integer, String
from db.base_class import Base

class User(Base):
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True)
  username = Column(String(40))
  email = Column(String(255))
  registered_on = Column(DateTime, default=datetime.datetime.utcnow)
  