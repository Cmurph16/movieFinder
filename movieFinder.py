#!/usr/local/bin/python3
import requests
import random

# get IMDb apikey
with open('imdb.key') as imdb_api_file:
    IMDB_API = imdb_api_file.read().splitlines()[0]

# IMDb top 250 URL
top_250_imdb_url = 'https://imdb-api.com/en/API/Top250Movies/{}'.format(IMDB_API)

# IMDb base movie URL 
base_imdb_url = 'https://www.imdb.com/title/'

# Make the API request and load the dictionary of the movies
response = requests.get(top_250_imdb_url)
json_top_250 = response.json()['items']

random_num = random.randint(0,249)
random_movie = json_top_250[random_num]
print('Your random movie picked is: {}. It came out in {} and has a {} on IMDb'.format(random_movie['title'], random_movie['year'], random_movie['imDbRating']))
print('Here is the IMDb page: {}'.format(base_imdb_url + random_movie['id']))

