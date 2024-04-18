from fastapi import FastAPI

app = FastAPI()

@app.get("/", description="This is first route.")
async def get():
  return {"message": "Hello World"}

@app.post("/")
async def post():
  return {"message": "Hello from post route"}

@app.put("/")
async def put():
  return {"message": "Hello from put route"}