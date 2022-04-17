#!/usr/local/bin/python3
import requests
import random
import json
from os.path import exists

def get_random_movie():
    with open('imdb.key') as imdb_api_file:
        IMDB_API = imdb_api_file.read().splitlines()[0]

    # IMDb top 250 URL
    top_250_imdb_url = 'https://imdb-api.com/en/API/Top250Movies/{}'.format(IMDB_API)

    # Make the API request and load the dictionary of the movies
    response = requests.get(top_250_imdb_url)
    json_top_250 = response.json()['items']

    # choose random movie from options
    random_num = random.randint(0,249)
    random_movie = json_top_250[random_num]
    return random_movie

def display_movie_info(movie):
    ''' Prints out movie picked
    '''
    # IMDb base movie URL 
    base_imdb_url = 'https://www.imdb.com/title/'

    print('Your random movie picked is: {}. It came out in {} and has a {} on IMDb'.format(movie['title'], movie['year'], movie['imDbRating']))
    print('Here is the IMDb page: {}'.format(base_imdb_url + movie['id']))

def log_movie(movie):
    WATCHED_MOVIE_LOG = 'movies.log'
    if exists(WATCHED_MOVIE_LOG):
        with open(WATCHED_MOVIE_LOG) as log_READ:
            log_json = json.load(log_READ)
        if movie['id'] in log_json:
            return 1
        else:
            log_json[movie['id']] = movie
            formatted_log = json.dumps(log_json)
            with open(WATCHED_MOVIE_LOG, 'w') as log_WRITE:
                log_WRITE.write(formatted_log)
            return 0
    else:
        log_json = {
            movie['id']: movie
        }
        formatted_log = json.dumps(log_json)
        with open(WATCHED_MOVIE_LOG, 'w') as log_WRITE:
                log_WRITE.write(formatted_log)
        return 0

def main():
    # get movie
    movie = get_random_movie()

    while log_movie(movie) != 0:
        movie = get_random_movie()
        
    # print movie
    display_movie_info(movie)

if __name__ == '__main__':
    main()