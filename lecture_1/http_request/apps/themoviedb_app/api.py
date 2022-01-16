#
#
#

import requests

key = "add here your api key"

url = "https://api.themoviedb.org/3/movie/popular"
params = {
    "api_key": key,
    "language": "en-US",
    "page": 1
}

data = requests.get(url, params).json()

print(data)

for index in range(len(data['results'])):
    print(f"\nMovie Name: {data['results'][index]['original_title']}"
          f"\nRelease Date: {data['results'][index]['release_date']}"
          f"\nPopularity: {data['results'][index]['popularity']}"
          f"\nVote Count: {data['results'][index]['vote_count']}"
          f"\nAverage Point: {data['results'][index]['vote_average']}"
          f"\nMovie Language: {data['results'][index]['original_language']}"
          )

# Movie Name: Sing 2
# Release Date: 2021-12-01
# Popularity: 9211.33
# Vote Count: 264
# Average Point: 7.5
# Movie Language: en


# Movie Name: Ghostbusters: Afterlife
# Release Date: 2021-11-11
# Popularity: 7227.726
# Vote Count: 753
# Average Point: 7.2
# Movie Language: en


# Movie Name: Spider-Man: No Way Home
# Release Date: 2021-12-15
# Popularity: 6708.051
# Vote Count: 4020
# Average Point: 8.4
# Movie Language: en
