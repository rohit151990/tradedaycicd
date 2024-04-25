from fastapi import APIRouter
from fastapi import Request
import os
router = APIRouter()



@router.get("/")
def home():
    return {"message": "This is second app "+os.environ.get('MY_NAME')}
@router.post("/items")
async def create_item(request: Request):
    data = await request.json()
    print('event data is ---------------------------')
    print(data)
    return data