from app.movie import format_movie_year_min
from app.movie import format_vote_average
from app.movie import format_runtime_min
from app.movie import format_runtime_max
from app.movie import format_movie_certification
from app.movie import genre_string_to_id

def test_movie_year_min():
    assert format_movie_year_min("1990") == "1990-01-01"
    assert format_movie_year_min("") == None

def test_vote_average():
    assert format_vote_average("7.2") == 7.2
    assert format_vote_average("") == None
    #assert format_vote_average("seven") == None
    #assert format_vote_average("seven") == "You entered an invalid value for the Minimum Movie Rating. Please try again"

def test_runtime_min():
    assert format_runtime_min("100") == 100
    assert format_runtime_min("") == None
    #assert format_runtime_min("tree") == "You entered an invalid value for the Minimum Runtime. Please try again"

def test_runtime_max():
    assert format_runtime_max("100") == 100
    assert format_runtime_max("") == None

def test_movie_certification():
    assert format_movie_certification("PG") == "PG"
    assert format_movie_certification("") == None

def test_genre_string_to_id():
    assert genre_string_to_id("Animation") == "16"
    assert genre_string_to_id("animation") == "16"
    assert genre_string_to_id("") == None