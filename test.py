import tmdbsimple as tmdb
import csv
import json
import os
import random

tmdb.API_KEY='c4c3cb40b87c5d67f381e5bbdc3763ca'

page_numbers = [1,2,3]
discover = tmdb.Discover()
for page_number in page_numbers:
    response = discover.movie(with_runtime_gte=140, with_runtime_lte=200, page=page_number)
    #response= discover.movie(with_cast="Adam Sandler")
    #print(response.keys())
    #print(response['results'].keys())
    values = []
    for value in response['results']:
        #print(value['title'])
        #print(value['release_date'])
        id = value['id']
        values.append(id)
        #print(value['id'])

    movie_list = []

    for value in values:
        movie = tmdb.Movies(value)
        response = movie.info()  
        runtime = movie.runtime
        title = movie.title
        movie_list.append(title)

n = 0
while n<3:
    movie_choice = random.choice(movie_list)
    print(movie_choice)
    movie_list.remove(movie_choice)
    n = n+1

