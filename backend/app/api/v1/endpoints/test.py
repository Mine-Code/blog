from fastapi import APIRouter, Depends

router = APIRouter(
  prefix="/test",
  tags=["test"],
)

@router.get("")
async def test():
  response = {
      "message": "hello world"
  }
  return response
