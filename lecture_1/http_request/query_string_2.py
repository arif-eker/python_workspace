#
#
#
#

# query string:
# "https://jsonplaceholder.typicode.com/todos?
# key1=value1&
# key2=value2&
# key3=value3....."

# with query string, we instead of getting all the data, we can pull the data that meets the condition we give.

import json

import requests

url = "https://jsonplaceholder.typicode.com/todos"

query_string = "https://jsonplaceholder.typicode.com/todos?userId=1"

query_string_true = "https://jsonplaceholder.typicode.com/todos?" \
                    "userId=1&" \
                    "completed=true"

query_string_false = "https://jsonplaceholder.typicode.com/todos?" \
                     "userId=1&" \
                     "completed=false"

resp = requests.get(query_string)
user1 = json.loads(resp.text)
len(user1)  # 20

resp = requests.get(query_string_true)
user1_true = json.loads(resp.text)
len(user1_true)  # 11

resp = requests.get(query_string_false)
user1_false = json.loads(resp.text)
len(user1_false)  # 9

# Another use still
resp = requests.get(query_string, params={"userId": 1,
                                          "completed": "true"})

data = json.loads(resp.text)
len(data)  # 11
