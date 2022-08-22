import json

data = {}

with open('App/paises.json', 'r') as file:
    data = json.load(file)

print(data)
print(data["AR"])