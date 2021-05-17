from flask import Blueprint, request, jsonify, render_template, redirect, flash

#from app.movie import set_movie_settings

movie_routes = Blueprint("movie_routes", __name__)
#
@movie_routes.route("/movie.json")
#def weather_forecast_api():
#    print("WEATHER FORECAST (API)...")
#    print("URL PARAMS:", dict(request.args))
#
#    country_code = request.args.get("country_code") or "US"
#    zip_code = request.args.get("zip_code") or "20057"
#
#    results = set_movie_settings #(country_code=country_code, zip_code=zip_code)
#    if results:
#        return jsonify(results)
#    else:
#        return jsonify({"message":"Invalid Geography. Please try again."}), 404
#
@movie_routes.route("/select/form")
def select_form():
    print("WEATHER FORM...")
    return render_template("form.html")
#
#@movie_routes.route("/weather/forecast", methods=["GET", "POST"])
#def weather_forecast():
#    print("WEATHER FORECAST...")
#
#    if request.method == "GET":
#        print("URL PARAMS:", dict(request.args))
#        request_data = dict(request.args)
#    elif request.method == "POST": # the form will send a POST
#        print("FORM DATA:", dict(request.form))
#        request_data = dict(request.form)
#
#    country_code = request_data.get("country_code") or "US"
#    zip_code = request_data.get("zip_code") or "20057"
#
#    results = get_hourly_forecasts(country_code=country_code, zip_code=zip_code)
#    if results:
#        flash("Weather Forecast Generated Successfully!", "success")
#        return render_template("weather_forecast.html", country_code=country_code, zip_code=zip_code, results=results)
#    else:
#        flash("Geography Error. Please try again!", "danger")
#        return redirect("/weather/form")