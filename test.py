import tmdbsimple as tmdb
import csv
import json
import os
import random

tmdb.API_KEY='c4c3cb40b87c5d67f381e5bbdc3763ca'

page_numbers = []

p = 1
while p<100:
    page_numbers.append(p)
    p = p + 1

discover = tmdb.Discover()
movie_ids = []
for page_number in page_numbers:
    response = discover.movie(sort_by="popularity.desc", with_genres=None, vote_average_gte=6.8, 
    primary_release_year=None, primary_release_date_gte=1980, with_runtime_gte=60, with_runtime_lte=180, 
    certification_country="US", certification=None, page=page_number)
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
    title = movie.title
    plot = movie.overview
    runtime = movie.runtime
    year = movie.release_date
    score = movie.vote_average
    genres = movie.genres

    print("Movie Name: " + str(title) + '\n')
    print("Additional Information")
    print("Overview: " + str(plot))
    print("Length: " + str(runtime) + " minutes")
    print("Release Date: " + str(year))
    print("Movie Rating: " + str(score) + "/10\n")
    print("Genre(s):")
    for genre in genres:
        print(genre['name'])
    print("\n")
        

