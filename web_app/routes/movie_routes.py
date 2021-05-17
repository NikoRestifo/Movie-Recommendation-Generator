#from app.main import RECEIVE_ADDRESS
from flask import Blueprint, request, jsonify, render_template, redirect, flash

movie_routes = Blueprint("movie_routes", __name__)
#

from app.movie import set_user_settings
from app.movie import format_movie_year_min
from app.movie import format_vote_average
from app.movie import format_runtime_min
from app.movie import format_runtime_max
from app.movie import format_movie_certification
from app.movie import genre_string_to_id
from app.movie import run_API

@movie_routes.route("/select.json")
def weather_forecast_api():
#    print("WEATHER FORECAST (API)...")
    print("URL PARAMS:", dict(request.args))

    movie_genre = request.args.get("genre") or None
    vote_average = request.args.get("vote_average") or None
    movie_year_min = request.args.get("movie_min_year") or None
    runtime_min = request.args.get("runime_min") or None
    runtime_max = request.args.get("runtime_max") or None
    movie_certification = request.args.get("rating") or None
#    USER_NAME = request.args.get("name") or None
#    RECIEVE_ADDRESS = request.args.get("email_address") or None
#    USER_NAME = request.args.get("name") or None
#    RECEIVE_ADDRESS = request.args.get("email_address") or None
    USER_NAME, RECIEVE_ADDRESS = set_user_settings(user_name, recieve_address)

    movie_year_min = format_movie_year_min(movie_year_min)
    vote_average = format_vote_average(vote_average)
    runtime_min = format_runtime_min(runtime_min)
    runtime_max = format_runtime_max(runtime_max)
    movie_certification = format_movie_certification(movie_certification)
    genre_number=genre_string_to_id(movie_genre)    
    results = run_API(movie_year_min, vote_average, runtime_min, runtime_max, movie_certification, genre_number, USER_NAME, RECIEVE_ADDRESS)
    
    if results:
        return jsonify({"message":"Invalid Inputs. Please try again."}), 404
    else:
        return jsonify({"message":"Email Sent!"})

# movie_year_min, vote_average, runtime_min, runtime_max, movie_certification, genre_number, USER_NAME, RECIEVE_ADDRESS
@movie_routes.route("/select")
def select_form():
    print("WEATHER FORM...")
    return render_template("select.html")
#
@movie_routes.route("/select/form", methods=["GET", "POST"])
def movie_forecast():
    print("WEATHER FORECAST...")

    if request.method == "GET":
        print("URL PARAMS:", dict(request.args))
        request_data = dict(request.args)
    elif request.method == "POST": # the form will send a POST
        print("FORM DATA:", dict(request.form))
        request_data = dict(request.form)

    #country_code = request_data.get("country_code") or "US"
    #zip_code = request_data.get("zip_code") or "20057"
    movie_genre = request_data.get("movie_genre")
    vote_average = request_data.get("vote_average")
    movie_year_min = request_data.get("movie_min_year")
    runtime_min = request_data.get("runime_min") 
    runtime_max = request_data.get("runtime_max")
    movie_certification = request_data.get("rating")
    USER_NAME = request_data.get("name")
    RECIEVE_ADDRESS = request_data.get("email_address")

    results = run_API(movie_year_min= movie_year_min, vote_average = vote_average, runtime_min = runtime_min, runtime_max = runtime_max, movie_certification= movie_certification, genre_number= movie_genre, USER_NAME= USER_NAME, RECIEVE_ADDRESS= RECIEVE_ADDRESS)
    if results == None:
        flash("Geography Error. Please try again!", "danger")
        return redirect("/select/form")
    else:
        flash("Successfully!", "success")
        return render_template("select_form.html", movie_year_min= movie_year_min, vote_average = vote_average, runtime_min = runtime_min, runtime_max = runtime_max, movie_certification= movie_certification, movie_genre = movie_genre, USER_NAME= USER_NAME, RECIEVE_ADDRESS=RECIEVE_ADDRESS, results=results)