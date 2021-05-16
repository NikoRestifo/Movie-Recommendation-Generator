import os
from dotenv import load_dotenv
from flask import Flask


load_dotenv()

APP_ENV = os.getenv("APP_ENV", default="development")

from web_app.routes.email import email
from web_app.routes.main import main
from web_app.routes.movie import movie

def create_app():
    app = Flask(__name__)
    app.config["APP_ENV"] = APP_ENV
    app.register_blueprint(email)
    app.register_blueprint(main)
    app.register_blueprint(movie)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)