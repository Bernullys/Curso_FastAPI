from fastapi import FastAPI, Path, Query

app = FastAPI()

"""
@app.get("/")
def home():
    return{"Data": "Test"} # this dict is automatic convert to json


@app.get("/about")
def about():
    return{"Data": "About"}
"""

# path parameters and query parameters:

example_inventory = {
    1: {
        "name": "milk",
        "price": 3.99,
        "brand": "regular"
    }
}

cars = {
    50: {
        "type": "offroad",
        "color": "green"
    }
}

#parameters:
@app.get("/get-item/{item_id}")
def get_item(item_id: int):
    return example_inventory[item_id]

# path parameters
@app.get("/get-car/{car_id}")
def get_car(car_id: int = Path(description="The ID of the item you'd like to buy is ", gt=0, lt=100)):
    return  cars[car_id]

# query parameters form: ?variable_name=some_value&some_other_value
@app.get("/get_info")
def get_whatever(name: str, test: int): # If I want to put a default value: def get_whatever(name: Optional[str] = None): Apart: the optional has to be the last or python will throw an error. Except we add *, then the parameters.
    for item_id in example_inventory:
        if example_inventory[item_id]["name"] == name:
            return example_inventory[item_id]
    return {"Data": "Not found"}

# convination of path parameter and query parameter:
@app.get("/get_info/{item_id}")
def get_whatever(name: str, brand: str, item_id: int):
    for item_id in example_inventory:
        if example_inventory[item_id]["name"] == name:
            return example_inventory[item_id]
    return {"Data": "Not found"}

