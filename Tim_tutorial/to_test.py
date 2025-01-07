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