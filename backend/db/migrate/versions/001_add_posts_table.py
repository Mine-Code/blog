from sqlalchemy import *
from migrate import *
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()
meta = MetaData()

class Post(Base):
  def __init__(self, meta):
    __metadata__ = meta

  __tablename__ = 'posts'

  id = Column(Integer, primary_key=True)
  user_id = Column(Integer, ForeignKey('users.id'))
  title = Column(String(100))
  body = Column(String(15000))
  created_at = Column(DateTime, default=datetime.datetime.utcnow)
  updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

class User(Base):
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True)
  username = Column(String(40))
  email = Column(String(255))

def upgrade(migrate_engine):
  # Upgrade operations go here. Don't create your own engine; bind
  # migrate_engine to your metadata

  meta.bind = migrate_engine
  Base.metadata.create_all(bind=migrate_engine)

def downgrade(migrate_engine):
  # Operations to reverse the above upgrade go here.
  pass
