from fastapi import FastAPI

my_application = FastAPI()

info = {
    "Bernardo": {
        "role": "husband",
        "age": 37
    },
    "Patricia": {
        "role": "wife",
        "age":34
    },
    "Joy": {
        "role": "Pet",
        "age": 7
    }
}

# A simple get endpoint:
@my_application.get("/this-is-my-address/")
def my_address():
    return(
        {
            "Info": "This is my simples endpoint"
        }
    )

# An endpoint using a simple query parameter:
@my_application.get("/find-family/")
def family_member(name: str):
    return (
        info[name]
    )

# An endpoint using multiple query parameters:
@my_application.get("/info/")
def get_info(age: int, role: str): # here we can also use multiples constrains.
    for person, details in info.items():
        if details.get("age") == age and details.get("role") == role:
            return person
    return (
        {
            "Data": "Not a family member"
        }
    )

# An endpoint usind a path parameter:
@my_application.get("/insert_name/{name}")
def insert_name(name: str):
    return (
        info[name]["role"], info[name]["age"]
    )

# A combination of path parameter with query parameter:
@my_application.get("/convination/{age}")
def convination(role: str, age: int):
    for person, details in info.items():
        if details.get("age") == age and details.get("role") == role:
            return person
    return (
        {
            "Data": "Age and role dont match"
        }
    )