from app.movie import format_movie_year_min
from app.movie import format_vote_average
from app.movie import format_runtime_min

def test_movie_year_min():
    assert format_movie_year_min("1990") == "1990-01-01"
    assert format_movie_year_min("") == None

def test_vote_average():
    assert format_vote_average("7.2") == 7.2
    assert format_vote_average("") == None
    assert format_vote_average("seven") == None
    #assert format_vote_average("seven") == "You entered an invalid value for the Minimum Movie Rating. Please try again"

def test_runtime_min():
    assert format_runtime_min("100") == 100
    assert format_runtime_min("") == None
    #assert format_runtime_min("tree") == "You entered an invalid value for the Minimum Runtime. Please try again"