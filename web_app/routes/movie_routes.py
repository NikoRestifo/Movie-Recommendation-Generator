from app.main import RECIEVE_ADDRESS, USER_NAME
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
#from app.movie import run_API

@movie_routes.route("/select.json")
def weather_forecast_api():
#    print("WEATHER FORECAST (API)...")
    print("URL PARAMS:", dict(request.args))
#
#    genre_number = request.args.get("genre") or "Adventure
#    zip_code = request.args.get("zip_code") or "20057"
#    movie_genre = request.args.get("genre") or None
#    vote_average = request.args.get("vote_average") or None
#    movie_year_min = request.args.get("movie_min_year") or None
#    runtime_min = request.args.get("runime_min") or None
#    runtime_max = request.args.get("runtime_max") or None
#    movie_certification = request.args.get("rating") or None
#    user_name = request.args.get("name") or None
#    receive_address = request.args.get("email_address") or None

    USER_NAME, RECIEVE_ADDRESS = set_user_settings(user_name, receive_address)
    #
    #movie_year_min = format_movie_year_min(movie_year_min)
    #vote_average = format_vote_average(vote_average)
    #runtime_min = format_runtime_min(runtime_min)
    #runtime_max = format_runtime_max(runtime_max)
    #movie_certification = format_movie_certification(movie_certification)
    #genre_number=genre_string_to_id(movie_genre)    
    #results = run_API(movie_year_min, vote_average, runtime_min, runtime_max, movie_certification, genre_number, USER_NAME, RECIEVE_ADDRESS)
    #
    if results:
        return jsonify({"message":"Invalid Inputs. Please try again."}), 404
    else:
        return jsonify({"message":"Email Sent!"})

# movie_year_min, vote_average, runtime_min, runtime_max, movie_certification, genre_number, USER_NAME, RECIEVE_ADDRESS
@movie_routes.route("/select")
def select_form():
    print("WEATHER FORM...")
    return render_template("form.html")
#
@movie_routes.route("/weather/forecast", methods=["GET", "POST"])
def weather_forecast():
    print("WEATHER FORECAST...")

    if request.method == "GET":
        print("URL PARAMS:", dict(request.args))
        request_data = dict(request.args)
    elif request.method == "POST": # the form will send a POST
        print("FORM DATA:", dict(request.form))
        request_data = dict(request.form)
#
    genre = request_data.get("genre") or "12"
#    zip_code = request_data.get("zip_code") or "20057"
# movie_year_min, vote_average, runtime_min, runtime_max, movie_certification, genre_number, USER_NAME, RECIEVE_ADDRESS
    results = run_API(genre_number=genre)
    if results:
        flash("Weather Forecast Generated Successfully!", "success")
        return render_template("weather_forecast.html", genre_number=genre, results=results)
    else:
        flash("Geography Error. Please try again!", "danger")
        return redirect("/select")