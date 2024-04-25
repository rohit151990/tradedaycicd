from fastapi import APIRouter
from fastapi import Request
import os
router = APIRouter()



@router.get("/")
def home():
    return {"message": str(os.environ.get('_PRIVATEKEY'))+"  --------------------- This is second app -------------------------"}
@router.post("/items")
async def create_item(request: Request):
    data = await request.json()
    print('event data is ---------------------------')
    print(data)
    return data