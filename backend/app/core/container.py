from dependency_injector import containers, providers

from app.core.config import configs
from app.core.database import Database
# from app.repository import *
# from app.services import *


class Container(containers.DeclarativeContainer):
  wiring_config = containers.WiringConfiguration(
    modules=[
      "app.api.v1.endpoints.test",
      "app.core.dependencies",
    ]
  )

  db = providers.Singleton(Database, db_url=configs.DATABASE_URI)

  # post_repository = providers.Factory(TestRepository, session_factory=db.provided.session)
