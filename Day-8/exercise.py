# import requests

# url = "https://api.open-meteo.com/v1/forecast"

# params = {
#     "latitude": 6.0329,
#     "longitude": 80.2168,
#     'current' : 'temperature_2m,wind_speed_10m'
# }
# def fetch_weather_data(latitude,longitude,wether_detail):
#     response = requests.get(url, params=params)

# # response = requests.get(url, params=params)
# data = response.json()

# print( data['current']['temperature_2m'])
# print( data['current']['wind_speed_10m'])

# import requests

# def get_weather(lat,long,current):
#     url = "https://api.open-meteo.com/v1/forecast"

#     params = {
#         "latitude": lat,
#         "longitude": long,
#         'current' : current
#     }

#     response = requests.get(url, params=params)
#     data = response.json()

#     return data['current']['temperature_2m'], data['current']['wind_speed_10m']

# print(get_weather(6.0329, 80.2168,'temperature_2m,wind_speed_10m'))

# Function to fetch weather data

# import requests

# def fetch_weather_data(latitude, longitude, current_info ='temperature_2m,wind_speed_10m'):
#     base_url = 'https://api.open-meteo.com/v1/forecast'
#     params = {
#         'latitude': latitude,
#         'longitude': longitude,
#         'current': current_info
#     }

#     response = requests.get(base_url, params=params)
    
#     if response.status_code == 200:
#         print('fetched data successfully')
#         pass_weather_data(response.json())
#     else: 
#         print('Error: ', response.status_code)

# # Function to show weather data    
# def pass_weather_data(data):
#     if data:
#         print('Temperature: ', data['current']['temperature_2m'], '°C')
#         print('Wind Speed: ', data['current']['wind_speed_10m'], 'km/h')
#     else:
#         print('Error fetching data')


# data = fetch_weather_data(6.9271, 79.8612, 'temperature_2m,wind_speed_10m')

# import pdb

def multiplication(a, b):
    answer = a * b
    return answer

# pdb.set_trace()
breakpoint()

x = input("Enter first number: ")
y = input("Enter second number: ")

mul = multiplication(x, y)
print(mul)