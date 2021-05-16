import tmdbsimple as tmdb
import csv
import json
import os
from dotenv import load_dotenv
import random
from app import APP_ENV
from genre_codes import genre_codes

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from datetime import date

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
SENDER_EMAIL_ADDRESS = os.getenv("SENDER_EMAIL_ADDRESS")
#USER_NAME = os.getenv("USER_NAME", default="Player 1")

load_dotenv()

def set_movie_settings():
    if APP_ENV == "development":
        movie_genre = str(input("Select Movie Genre: "))
        vote_average = str(input("Minimum Movie Rating: "))
        #movie_year_min = str(input("Movies Released in Year: "))
        movie_year_min = str(input("Movies Release After Year: "))
        runtime_min = str(input("Minimum Runtime: "))
        runtime_max = str(input("Maximum Runtime: "))
        movie_certification = str(input("Enter Movie Certification: "))
        #movie_year_start = input("Movies Released After Year:")
    #else:
    #    user_country = COUNTRY_CODE
    #    user_zip = ZIP_CODE
    return movie_genre, vote_average, movie_year_min, runtime_min, runtime_max, movie_certification

pick_movie_genre, pick_vote_average, pick_movie_year_min, pick_runtime_min, pick_runtime_max, pick_certification = set_movie_settings()

def set_user_settings():
    if APP_ENV == "development":
        USER_NAME = input("Please enter your name: ")
        RECIEVE_ADDRESS = input("Please enter your email address: ")
    return USER_NAME, RECIEVE_ADDRESS

USER_NAME, RECIEVE_ADDRESS = set_user_settings()

def send_email(subject="[Daily Briefing] This is a test", html="<p>Hello World</p>", recipient_address=RECIEVE_ADDRESS):
    """
    Sends an email with the specified subject and html contents to the specified recipient,

    If recipient is not specified, sends to the admin's sender address by default.
    """
    client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
    print("CLIENT:", type(client))
    print("SUBJECT:", subject)
    #print("HTML:", html)

    message = Mail(from_email=SENDER_EMAIL_ADDRESS, to_emails=recipient_address, subject=subject, html_content=html)
    try:
        response = client.send(message)
        print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
        print(response.status_code) #> 202 indicates SUCCESS
        return response
    except Exception as e:
        print("OOPS", type(e), e.message)
        return None
    
tmdb.API_KEY='c4c3cb40b87c5d67f381e5bbdc3763ca'

#Genre = os.getenv("COUNTRY_CODE", default="US")
#ZIP_CODE = os.getenv("ZIP_CODE", default="20057")

def format_movie_year_min(pick_movie_year_min):
    if bool(pick_movie_year_min) == True:
        movie_year_min = str(pick_movie_year_min) + "-01-01"
    else:
        movie_year_min = None
    return movie_year_min

movie_year_min = format_movie_year_min(pick_movie_year_min)

def format_vote_average(pick_vote_average):
    if bool(pick_vote_average) == True:
        vote_average = float(pick_vote_average)
    else:
        vote_average = None
    return vote_average

vote_average = format_vote_average(pick_vote_average)

def format_runtime_min(pick_runtime_min):
    if bool(pick_runtime_min) == True:
        runtime_min = int(pick_runtime_min)
    else:
        runtime_min = None
    return runtime_min

runtime_min = format_runtime_min(pick_runtime_min)

def format_runtime_max(pick_runtime_max):
    if bool(pick_runtime_max) == True:
        runtime_max = int(pick_runtime_max)
    else:
        runtime_max = None
    return runtime_max

runtime_max = format_runtime_max(pick_runtime_max)

def format_movie_certification(pick_certification):
    if bool(pick_certification) == True:
        movie_certification= str(pick_certification)
    else:
        movie_certification = None
    return movie_certification

movie_certification = format_movie_certification(pick_certification)

def genre_string_to_id():
    ids_list = []
    genre_select = genre_codes['genres']
    for genre in genre_select:
        if genre['name'] == pick_movie_genre:
            genre_id = str(genre['id'])
            ids_list.append(genre_id)
            break
    if not ids_list:
        genre_id = None
    return genre_id

genre_number=genre_string_to_id()

page_numbers = []

def run_API(movie_year_min, vote_average, runtime_min, runtime_max, movie_certification, genre_number, USER_NAME):
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

run_API(movie_year_min, vote_average, runtime_min, runtime_max, movie_certification, genre_number, USER_NAME)




