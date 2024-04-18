from enum import Enum

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


@app.get("/users")
async def list_users():
    return {"message": "list users route"}


@app.get("/users/me")
async def get_current_user():
    return {"message": "This is current user."}


@app.get("/users/{user_id}")
async def user_id(user_id: str):
    return {"user_id": user_id}


class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"


@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.vegetables:
        return {"food_name": food_name, "message": "You're healthy"}

    if food_name.value == "fruits":
        return {"food_name": food_name, "message": "You're still healthy"}

    return {"food_name": food_name, "message": "You're not so healthy bro. Come on!!!"}
