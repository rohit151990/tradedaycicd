from fastapi import FastAPI


from fastapi import Request
app = FastAPI()



@app.get("/")
def home():
    return {"message": "This is second  app"}
@app.post("/items")
async def create_item(request: Request):
    data = await request.json()
    print('event data is ---------------------------')
    print(data)
    return data