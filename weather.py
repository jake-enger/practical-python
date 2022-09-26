import requests

api_key = "96bc644ae3a9056504c56648996ba15e"
city = "Riverton"

url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=imperial"

request = requests.get(url)
json = request.json()

description = json.get("weather")[0].get("description")
print("Today's forecast is", description)

temp_min = json.get("main").get("temp_min")
print("The minimum temperature is", temp_min)

temp_max = json.get("main").get("temp_max")
print("The max temperature for today is", temp_max)