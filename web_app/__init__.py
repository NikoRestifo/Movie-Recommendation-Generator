
import os
from dotenv import load_dotenv
from flask import Flask

from web_app.routes.main_routes import main_routes
from web_app.routes.movie_routes import movie_routes

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", default="super secret") # set this to something else on production!!!

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = SECRET_KEY
    app.register_blueprint(main_routes)
    app.register_blueprint(movie_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)