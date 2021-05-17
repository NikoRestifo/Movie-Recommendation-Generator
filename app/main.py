from app.movie import set_movie_settings
from app.movie import set_user_settings
from app.movie import format_movie_year_min
from app.movie import format_vote_average
from app.movie import format_runtime_min
from app.movie import format_runtime_max
from app.movie import format_movie_certification
from app.movie import genre_string_to_id
from app.movie import run_API


pick_movie_genre, pick_vote_average, pick_movie_year_min, pick_runtime_min, pick_runtime_max, pick_certification = set_movie_settings()

USER_NAME, RECIEVE_ADDRESS = set_user_settings()

try:
    movie_year_min = format_movie_year_min(pick_movie_year_min)

    vote_average = format_vote_average(pick_vote_average)

    runtime_min = format_runtime_min(pick_runtime_min)

    runtime_max = format_runtime_max(pick_runtime_max)

    movie_certification = format_movie_certification(pick_certification)

    genre_number=genre_string_to_id(pick_movie_genre)    

    run_API(movie_year_min, vote_average, runtime_min, runtime_max, movie_certification, genre_number, USER_NAME, RECIEVE_ADDRESS)

except:
    print("OOPS ran into error")
