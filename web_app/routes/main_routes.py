# web_app/routes/main_routes.py

from flask import Blueprint, request, render_template

main_routes = Blueprint("main_routes", __name__)

@main_routes.route("/")
@main_routes.route("/welcome")
def index():
    print("HOME...")
    #return "Welcome Home"
    return render_template("welcome.html")

@main_routes.route("/about")
def about():
    print("ABOUT...")
    return render_template("about.html")

@main_routes.route("/select")
def hello_world():
    print("HELLO...", dict(request.args))
    name = request.args.get("name") or "World"
    message = f"Hello, {name}!"
    return render_template("select.html", message=message)