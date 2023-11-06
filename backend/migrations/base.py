from app.model.base_model import BaseSQLModel

# すべてのモデルをimport (alembicにモデル情報を引き渡すために必要)
from app.model.user import User
from app.model.user_auth import UserAuth
