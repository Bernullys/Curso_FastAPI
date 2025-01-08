from fastapi import FastAPI
from pydantic import BaseModel
# pydantic validate the incoming data automatically

application = FastAPI()

class Person(BaseModel):
    nick_name: str
    age: int
    size: float

# This will be a dict of instances of class Person
# This should be a database
persons_intances = {}

# Basic way of posting info:
@application.post("/persons/")
def persons(person: Person):
    return {
        "message": "Person added successfully",
        "person": person
    }

# Adding persons details we the person name as a key of the dictionary details:
@application.post("/add_details_by_person/{person_name}")
def add_details(person_name: str, person: Person):
    persons_intances[person_name] = person
    return persons_intances[person_name]

# This is an endpoint to get (check) the persons I'm posting before (which will be storing on dict persons_instances)
@application.get("/check_person_posted")
def check_person(nick_name):
    for person in persons_intances:
        if persons_intances[person].nick_name == nick_name:
            return persons_intances[person]

# This is and endpoint to update the details of a person instance
@application.put("/updating/{person_name}")
def updating_person(person_name: str, person: Person):
    if person.nick_name != None:
        persons_intances[person_name].nick_name = person.nick_name
    if person.age != None:
        persons_intances[person_name].age = person.age
    if person.size != None:
        persons_intances[person_name].size = person.size

    return persons_intances[person_name]

# This endpoint is to delete a person instance
@application.delete("/deleting/{person_name}")
def deleting_person(person_name: str):
    del persons_intances[person_name]
    return {"Success": "Person deleted!"}