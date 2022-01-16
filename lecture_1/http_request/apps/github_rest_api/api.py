#
#
#

import requests

url = "https://api.github.com/users/"

username = "arif-eker"

user_data = requests.get(url + username)

data = user_data.json()

print(dict(data).keys())

for u in data:
    print(u, ": ", data[u])

print(f"\nUsername: {data['login']}"
      f"\nReal Name: {data['name']}"
      f"\nBlog: {data['blog']}"
      f"\nPublic Repo Count: {data['public_repos']}"
      f"\nFollowers: {data['followers']}"
      f"\nFollowing: {data['following']}")

# Create a repository

my_token = "add_your_acces_token_"

post_url = "https://api.github.com/user/repos"
new_data = {"name": "deneme",
            "private": True}
token = {'Authorization': 'token ' + my_token}
new_repo = requests.post(post_url, json=new_data, headers=token)
print(new_repo.status_code)

###########################
# Delete repo

delete_url = "https://api.github.com//repos/arif-eker/deneme"

del_repo = requests.delete(delete_url, headers=token)
print(del_repo.status_code)

# remember, token must be accept your delete request . look combo box :)
