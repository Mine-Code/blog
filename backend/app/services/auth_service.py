from datetime import timedelta
from typing import List

from app.core.config import configs
from app.core.exceptions import AuthError
from app.core.security import create_access_token, get_credential_hash, verify_credential
from app.model.user import User
from app.model.user_auth import UserAuth
from app.repository.user_repository import UserRepository
from app.repository.user_auth_repository import UserAuthRepository
from app.schema.auth_schema import Payload, SignIn, SignUp
from app.schema.user_schema import FindUserAuth
from app.services.base_service import BaseService
from app.util.hash import get_rand_hash


class AuthService(BaseService):
  def __init__(self, user_repository: UserRepository, user_auth_repository: UserAuthRepository):
    self.user_repository = user_repository
    self.user_auth_repository = user_auth_repository
    super().__init__(user_repository)

  def sign_in(self, sign_in_info: SignIn):
    find_user = FindUserAuth()
    find_user.identity_type__eq = sign_in_info.identity_type__eq
    find_user.identifier__eq = sign_in_info.identifier__eq
    user_auths: List[UserAuth] = self.user_auth_repository.read_by_options(find_user)["founds"]
    
    if len(user_auths) < 1:
      raise AuthError(detail="Incorrect identity type or identifier")
    found_user_auth = user_auths[0]

    # if not found_user_auth.is_active:
    #   raise AuthError(detail="Account is not active")

    if found_user_auth.identity_type == "email":
      if not verify_credential(sign_in_info.password, found_user_auth.password):
        raise AuthError(detail="Incorrect email or password")
    
      # delattr(found_user_auth, "password")

      matched_users: List[User] = self.user_repository.read_by_id(found_user_auth.user_id)["founds"]
      
      if len(matched_users) < 1:
        raise AuthError(detail="User not found")
      
      found_user = matched_users[0]

      payload = Payload(
        id=found_user.id,
        identity_type=found_user_auth.identity_type,
        identifier=found_user_auth.identifier,
        username=found_user.username,
        # is_superuser=found_user_auth.is_superuser,
      )

      token_lifespan = timedelta(minutes=configs.ACCESS_TOKEN_EXPIRE_MINUTES)
      access_token, expiration_datetime = create_access_token(payload.dict(), token_lifespan)
      sign_in_result = {
        "access_token": access_token,
        "expiration": expiration_datetime,
        "user_info": found_user_auth,
      }
      return sign_in_result
    
    elif found_user_auth.identity_type == "github":
      # TODO: implement github sign in
      pass
    else:
      raise AuthError(detail="Incorrect identity type")

  def sign_up(self, user_info: SignUp):
    if user_info.identity_type == "email":
      user_token = get_rand_hash()
      # user = User(**user_info.dict(exclude_none=True), is_active=True, is_superuser=False, user_token=user_token)
      user = User(**user_info.dict(exclude_none=True), user_token=user_token)
      
      hashed_credential = get_credential_hash(user_info.raw_credential)
      user_auth = UserAuth(
        **user_info.dict(exclude_none=True),
        identity_type="email",
        identifier=user_info.identifier,
        credential=hashed_credential
      )

      delattr(user_auth, "raw_credential")
      
      created_user_auth = self.user_auth_repository.create(user_auth)
      created_user = self.user_repository.create(user)

      return created_user
    
    elif user_info.identity_type == "github":
      # TODO: implement github sign up
      pass
    else:
      raise AuthError(detail="Incorrect identity type")
