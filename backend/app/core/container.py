from dependency_injector import containers, providers

from app.core.config import configs
from app.core.database import Database
from app.repository import *
from app.services import *


class Container(containers.DeclarativeContainer):
  wiring_config = containers.WiringConfiguration(
    modules=[
      "app.api.v1.endpoints.user",
      "app.core.dependencies",
    ]
  )

  db = providers.Singleton(Database, db_url=configs.DATABASE_URI)

  user_repository = providers.Factory(UserRepository, session_factory=db.provided.session)
  user_service = providers.Factory(UserService, repository=user_repository)  
