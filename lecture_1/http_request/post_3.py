#
#

import json
import requests

new_data = {
    "userId": 15,
    "title": "NEW_TITLE",
    "body": "Hello, it's my new post requests!"
  }

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.post(url, data=new_data)

print(response)  # <Response [201]>    ------> it worked :)

print(response.text)
# Output:
# {
#   "userId": "15",
#   "title": "NEW_TITLE",
#   "body": "Hello, it's my new post requests!",
#   "id": 101
# }