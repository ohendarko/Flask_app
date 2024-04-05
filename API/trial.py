import requests
import json

response = requests.get('https://swapi-api.alx-tools.com/api/films')

for data in response.json()['results']:
    print(data['episode_id'])
    print(data['title'])
