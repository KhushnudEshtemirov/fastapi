from enum import Enum

from fastapi import FastAPI, Query
from pydantic import BaseModel

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


fake_item_db = [
    {"item_name": "Car"},
    {"item_name": "Bus"},
    {"item_name": "Train"},
    {"item_name": "Plane"},
]


@app.get("/vehicles")
async def list_vehicles(skip: int = 0, limit: int = 10):
    return fake_item_db[skip : skip + limit]


@app.get("/items/{item_id}")
async def get_item(
    item_id: str, sample_query_param: str, q: str | None = None, short: bool = True
):
    item = {"item_id": item_id, "sample_query_param": sample_query_param}
    if q:
        item.update({"query": q})
    if not short:
        item.update(
            {
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras quam."
            }
        )
    return item


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.post("/items")
async def create_item(item: Item):
    item_dict = item.model_dump()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


@app.get("/items")
async def read_items(q: str | None = Query(None, min_length=3, max_length=10)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
