import tmdbsimple as tmdb
import csv
import json
import os
import random

tmdb.API_KEY='c4c3cb40b87c5d67f381e5bbdc3763ca'

page_numbers = []

p = 1
while p<75:
    page_numbers.append(p)
    p = p + 1

discover = tmdb.Discover()
movie_ids = []
for page_number in page_numbers:
    response = discover.movie(with_runtime_gte=80, with_runtime_lte=180, primary_release_year=None, primary_release_date_gte=1990,
    primary_release_date_lte=None, with_genres=None, page=page_number)
    for value in response['results']:
        id = value['id']
        movie_ids.append(id)
    
movies_list = []

n = 0
while n<3:
    movie_choice = random.choice(movie_ids)
    movies_list.append(movie_choice)
    movie_ids.remove(movie_choice)
    n = n+1

for single_movie in movies_list:
    movie = tmdb.Movies(single_movie)
    response = movie.info()  
    runtime = movie.runtime
    title = movie.title
    year = movie.release_date
    score = movie.vote_average
    genres = movie.genres

    print("Movie Name: " + str(title) + '\n')
    print("Additional Information")
    print("Length: " + str(runtime) + " minutes")
    print("Release Date: " + str(year))
    print("Movie Rating: " + str(score) + "/10\n")
    print("Genre(s):")
    for genre in genres:
        print(genre['name'])
    print("\n")
        