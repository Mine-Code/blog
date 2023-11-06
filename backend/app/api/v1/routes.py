from fastapi import APIRouter

from .endpoints.test import router as test_router
from .endpoints.user import router as user_router
from .endpoints.auth import router as auth_router

routers = APIRouter()
router_list = [test_router, user_router, auth_router]

for router in router_list:
  router.tags = routers.tags.append("v1")
  routers.include_router(router)
