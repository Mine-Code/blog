from fastapi import APIRouter, Depends

from app.schema.test_schema import TestResponse

router = APIRouter(
  prefix="/test",
  tags=["test"],
)

@router.get("", response_model=TestResponse)
async def test():
  return {"message": "test"}
