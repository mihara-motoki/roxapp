from fastapi import FastAPI

app = FastAPI()

@app.get('/hello')
async def hello():
	return {"test": "hello world!"}

@app.get("/name/{name}")
def get_muname(name: str):
	return {"name": name}

item_data = {"1": "banana", "2": "kiwi", "3": "range"}

# @app.get("/item/{no}")
# def item(no):
# 	return {"no": no, "name": item_data[no]}

@app.get("/sum")
def sum(x: int, y: int):
	return {x + y}

from pydantic import BaseModel

class Item(BaseModel):
    no: int
    name: str
    price: int

@app.post("/items/")
def create_item(item: Item):
    return 