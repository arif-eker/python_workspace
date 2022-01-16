#
#
# pip install requests

import requests

url = "https://jsonplaceholder.typicode.com/todos"

response = requests.get(url)

print(response)  # Output: <Response [200]>

print(response.status_code)  # Output: 200
print(response.headers)
response.__sizeof__()  # 32 bytes
print(response.encoding)  # utf-8

print(response.content)

print(response.text)
# [
#   {
#     "userId": 1,
#     "id": 1,
#     "title": "delectus aut autem",
#     "completed": false
#   },
#   {
#     "userId": 1,
#     "id": 2,
#     "title": "quis ut nam facilis et officia qui",
#     "completed": false
#   },
#   ...,
#   ...
# ]


import json

type(response.text)  # <class 'str'>
# so use json.loads()
data = json.loads(response.text)

type(data)  # <class 'list'>
print((data[0]))  # {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
