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

print(info["Bernardo"]["role"])

for person, details in info.items():
    print(person, details.get("role"))

class Person():
    def __init__(self, nick_name, age, tall):
        self.nick_name = nick_name
        self.age = age
        self.tall = tall


Bernardo = Person("naro", 37, 1.72)

print(Bernardo)

for person in info:
    if info[person] == "Bernardo":
        print(person, info[person])

for person in info:
    print(person, info[person])