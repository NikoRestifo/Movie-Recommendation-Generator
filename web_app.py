import csv
import json
import os
import datetime
import seaborn as sns
import matplotlib.pyplot as plt

from dotenv import load_dotenv
import requests
from pandas import read_csv


import tmdbsimple as tmdb
tmdb.API_KEY='c4c3cb40b87c5d67f381e5bbdc3763ca'
#search = tmdb.Search()
#Userinput=input('Enter first movie name:')
#response = search.movie(query=Userinput)
#Userinput2=input('Enter Second movie name:')
#response = search.movie(query=Userinput2)
#for s in (search.results):
# print(s['title'], s['popularity'])
#
#cal_start_date_str = '2014-12-11'
#cal_end_date_str = '2014-12-12'
discover = tmdb.Discover()
results = discover.movie(
    with_keywords = input("please select")
#    release_date_gte=cal_start_date_str,
#    release_date_lte=cal_end_date_str,
#    sort_by="release_date.asc",
)
#
for movie in results["results"]:
    print("=" * 40)
    print(movie["title"])
    print(movie["id"])
    print(movie["release_date"])
    # Get the release dates for the movie
    response = tmdb.movies.Movies(movie["id"]).release_dates()
    results = response["results"][0]
    release_dates = results["release_dates"]

    for release in release_dates:
        print("-" * 40)
        print(f"release: {release}")
        release_date_string = release["release_date"]
        print(f"release_date_string: {release_date_string}")
        # Check if this release date is in the range specified
        release_datetime_begin = datetime.datetime.strptime(release["release_date"], "%Y-%m-%dT00:00:00.000Z")
        release_date_begin = release_datetime_begin.date()
        print(f"release_date_begin: {release_date_begin}")