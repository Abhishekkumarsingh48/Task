import requests
api_key="db81cadbb701d88663eea2ea7bf716e8"
city = input('Enter city name: ')

url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    print(f'Temperature: {temp} K')
    print('Humidity is:',data['main']['humidity'])
    print(f'Description: {desc}')
else:
    print('Error fetching weather data')
