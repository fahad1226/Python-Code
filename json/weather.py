import requests

api_address = "https://api.openweathermap.org/data/2.5/weather?appid=51dfc962a5f58d715b2dd9c5e347b8e0&q="

city = input('enter city name: ')

url = api_address + city
json_data = requests.get(url).json()
formatted_data = json_data['weather'][0]['description']
print(f'Todays weather in your {city} city')
print(formatted_data)
