import requests

people = requests.get('https://api.open-notify.org/astros.json')
json = people.json()

print(json)

print("The people in space currently are:")
for p in json["people"]:
    print(p["name"])