import tmdbsimple as tmdb
import os
from dotenv import load_dotenv
import random
from app import APP_ENV
from genre_codes import genre_codes
from app.email import SENDER_EMAIL_ADDRESS, send_email
from datetime import date



load_dotenv()

GENRE = os.getenv("GENRE", default=None)
VOTE_AVERAGE = os.getenv("VOTE_AVERAGE", default=None)
MOVIE_MINIMUM_YEAR = os.getenv("MOVIE_MINIMUM_YEAR", default=None)
RUNTIME_MINIMUM = os.getenv("RUNTIME_MINIMUM", default=None)
RUNTIME_MAXIMUM = os.getenv("RUNTIME_MAXIMUM", default=None)
MOVIE_CERT = os.getenv("MOVIE_CERT", default=None)
MOVIE_CERT = os.getenv("MOVIE_CERT", default=None)
NAME = os.getenv("NAME", default="Movie Lover")
USER_EMAIL = os.getenv("USER_EMAIL", default=SENDER_EMAIL_ADDRESS)
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

def set_movie_settings():
    if APP_ENV == "development":
        movie_genre = str(input("Select Movie Genre: "))
        vote_average = str(input("Minimum Movie Rating: "))
        movie_year_min = str(input("Movies Release After Year: "))
        runtime_min = str(input("Minimum Runtime: "))
        runtime_max = str(input("Maximum Runtime: "))
        movie_certification = str(input("Enter Movie Certification: "))
    else:
        movie_genre = GENRE
        vote_average = VOTE_AVERAGE
        movie_year_min = MOVIE_MINIMUM_YEAR
        runtime_min = RUNTIME_MINIMUM
        runtime_max = RUNTIME_MAXIMUM
        movie_certification = MOVIE_CERT
    return movie_genre, vote_average, movie_year_min, runtime_min, runtime_max, movie_certification

def set_user_settings():
    if APP_ENV == "development":
        USER_NAME = input("Please enter your name: ")
        RECIEVE_ADDRESS = input("Please enter your email address: ")
    else:
        USER_NAME = NAME
        RECIEVE_ADDRESS = USER_EMAIL
        
    return USER_NAME, RECIEVE_ADDRESS

tmdb.API_KEY=TMDB_API_KEY

def format_movie_year_min(pick_movie_year_min):
    if bool(pick_movie_year_min) == True:
            movie_year_min = str(pick_movie_year_min) + "-01-01"
    else:
        movie_year_min = None
    return movie_year_min


def format_vote_average(pick_vote_average):
    try:
        if bool(pick_vote_average) == True:
            vote_average = float(pick_vote_average)
        else:
            vote_average = None
    except(ValueError):
        print("You entered an invalid value for the Minimum Movie Rating. Please try again.")
        quit()
    return vote_average

def format_runtime_min(pick_runtime_min):
    try:
        if bool(pick_runtime_min) == True:
            runtime_min = int(pick_runtime_min)
        else:
            runtime_min = None
    except(ValueError):
        print("You entered an invalid value for the Minimum Runtime. Please try again")
        quit()  
    return runtime_min

def format_runtime_max(pick_runtime_max):
    try:
        if bool(pick_runtime_max) == True:
            runtime_max = int(pick_runtime_max)
        else:
            runtime_max = None
    except(ValueError):
        print("You entered an invalid value for the Maximum Runtime. Please try again")
        quit()
    return runtime_max

def format_movie_certification(pick_certification):
    if bool(pick_certification) == True:
        movie_certification= str(pick_certification)
    else:
        movie_certification = None
    return movie_certification

def genre_string_to_id(pick_movie_genre):
    ids_list = []
    genre_select = genre_codes['genres']
    for genre in genre_select:
        if genre['name'].lower() == pick_movie_genre.lower():
            genre_id = str(genre['id'])
            ids_list.append(genre_id)
            break
    if not ids_list:
        genre_id = None
    return genre_id


def run_API(movie_year_min, vote_average, runtime_min, runtime_max, movie_certification, genre_number, USER_NAME, RECIEVE_ADDRESS):
    page_numbers = []
    p = 1
    while p<100:
        page_numbers.append(p)
        p = p + 1
    
    discover = tmdb.Discover()
    movie_ids = []
    for page_number in page_numbers:
        response = discover.movie(sort_by="popularity.desc", with_genres=genre_number, vote_average_gte=vote_average, 
        primary_release_year=None, primary_release_date_gte=movie_year_min, with_runtime_gte=runtime_min, with_runtime_lte=runtime_max, 
        certification_country="US", certification=movie_certification, page=page_number)
        for value in response['results']:
            id = value['id']
            movie_ids.append(id)
        
    movies_list = []

    if len(movie_ids) == 0:
            print("Data could not be retrieved. Please try again")
            return None

    n = 0
    while n<3:
        movie_choice = random.choice(movie_ids)
        movies_list.append(movie_choice)
        movie_ids.remove(movie_choice)
        n = n+1

    todays_date = date.today().strftime('%A, %B %d, %Y')
    html = ""
    html += f"<h3>Good Morning, {USER_NAME}!</h3>"
    html += "<h4>Today's Date</h4>"
    html += f"<p>{todays_date}</p>"
    html += f"<h4>Todays Movie Recomendations:</h4>"

    for single_movie in movies_list:
        movie = tmdb.Movies(single_movie)
        response = movie.info()  
        title = movie.title
        plot = movie.overview
        runtime = movie.runtime
        year = movie.release_date
        score = movie.vote_average
        genres = movie.genres
        poster = movie.poster_path

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
        
        html += "<ul>"
        html += f"<img src='https://image.tmdb.org/t/p/original/{poster}' alt='Movie Poster' width='500' height='600'>"
        html += f"<h3>Movie Name: {title} <h2>"
        html += f"<h4>Additional Information<h4>"
        html += f"<p>Overview: {plot}<p>"
        html += f"<p>Length: {runtime} minutes<p>"
        html += f"<p>Release Date: {year}<p>"
        html += f"<p>Movie Rating: {score}/10 <p>"
        html += f"<h4>Genre(s):<h4>"
        for genre in genres:
            html += f"<li> {genre['name']}</li>"
        html += "</ul>"

    send_email(subject="[Daily Briefing] Movie Time", html=html, recipient_address=RECIEVE_ADDRESS)





