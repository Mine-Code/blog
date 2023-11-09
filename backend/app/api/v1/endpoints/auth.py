from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.core.container import Container
from app.core.dependencies import get_current_active_user
from app.model.user import User
from app.schema.auth_schema import AuthsWithUser, SignIn, SignInResponse, SignUp, RawIdentifier
from app.services.auth_service import AuthService

router = APIRouter(
  prefix="/auth",
  tags=["auth"],
)


@router.post("/sign-in", response_model=SignInResponse)
@inject
async def sign_in(
  user_info: SignIn,
  service: AuthService = Depends(Provide[Container.auth_service])):
  return service.sign_in(user_info)

@router.post("/sign-up", response_model=User)
@inject
async def sign_up(
  user_info: SignUp,
  service: AuthService = Depends(Provide[Container.auth_service])):
  return service.sign_up(user_info)

@router.post("/register", response_model=AuthsWithUser)
@inject
async def register(
  register_info: RawIdentifier,
  current_user: User = Depends(get_current_active_user),
  service: AuthService = Depends(Provide[Container.auth_service])):
  return service.register(register_info, current_user)

@router.get("/me", response_model=User)
@inject
async def get_me(current_user: User = Depends(get_current_active_user)):
  user = User()
  user.username = current_user.username
  user.uuid = current_user.uuid
  user.created_at = current_user.created_at
  user.updated_at = current_user.updated_at
  user.is_active = current_user.is_active
  user.is_superuser = current_user.is_superuser
  user.id = current_user.id
  return user
