import requests

response = requests.get("http://api.open-notify.org/astros.json")

json = response.json()
print(json)

print("The people in space currently are:")
for person in json["people"]:
    