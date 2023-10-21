from fastapi import APIRouter

from .endpoints.test import router as test_router

routers = APIRouter()
router_list = [test_router]

for router in router_list:
  router.tags = routers.tags.append("v1")
  routers.include_router(router)
