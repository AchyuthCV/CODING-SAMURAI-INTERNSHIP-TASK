import requests

city_name = input("Enter city name: ")
API_key = "0eb33b90412ae89ceca88903fafe5dd2"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Temperature:", data["main"]["temp"], "°C")
    print("Humidity:", data["main"]["humidity"], "%")
    print("Weather:", data["weather"][0]["description"])
else:
    print("Error:", response.status_code)
    print(response.text)

