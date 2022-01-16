#
#
#

import requests

url = "http://api.weatherapi.com/v1/current.json"
api_key = "637745983e11422fad8102346201911"

response = requests.get(url, params={"key": api_key,
                                     "q": "istanbul",
                                     "lang": "tr"
                                     })

print(response.status_code)  # 200

data = response.json()

for i in response.json().keys():
    print("key:", i)
# key: location
# key: current

print(f"Date: {data['location']['localtime']}"
      f"\nCountry: {data['location']['country']}"
      f"\nCity: {data['location']['name']}"
      f"\nWeather Text: {data['current']['condition']['text']}"
      f"\nTemp (C): {data['current']['temp_c']}"
      f"\nTemp (F): {data['current']['temp_f']}"
      f"\nFeelslike (C): {data['current']['feelslike_c']}"
      f"\nFeelslike (C): {data['current']['feelslike_f']}")

# Date: 2022-01-17 2:40
# Country: Turkey
# City: Istanbul
# Weather Text: Açık
# Temp (C): 3.0
# Temp (F): 37.4
# Feelslike (C): 1.5
# Feelslike (C): 34.7
