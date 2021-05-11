import csv
import json
import os

import tmdbsimple as tmdb
tmdb.API_KEY='c4c3cb40b87c5d67f381e5bbdc3763ca'

#search by name example
#search = tmdb.Search()
#Userinput=input('Enter first movie name:')
#response = search.movie(query=Userinput)
#for s in (search.results):
#    print(s['title'], s['popularity'])
#

#discover by year, list
#discover = tmdb.Discover()
#response2 = discover.movie(year=2017)
#for value in response2['results']:
#    print(value['title'])
#print(len(response2['results']))
#

#not working but close, hard website example
import requests
response3 = requests.get('https://api.themoviedb.org/3/discover/movie?api_key=c4c3cb40b87c5d67f381e5bbdc3763ca&sort_by=popularity.asc')
popularity = response3.json()
top_popular = popularity['results']
top_popular[0:2]
print(popularity)

