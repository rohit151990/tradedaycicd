from fastapi import APIRouter
from fastapi import Request
router = APIRouter()



@router.get("/")
def home():
    return {"message": "This is second app"}
@router.post("/items")
async def create_item(request: Request):
    data = await request.json()
    print('event data is ---------------------------')
    print(data)
    return data