import os
import pytest
from app.movie import format_movie_year_min
from app.movie import format_vote_average
from app.movie import format_runtime_min
from app.movie import format_runtime_max
from app.movie import format_movie_certification
from app.movie import genre_string_to_id
from app.movie import run_API
from app.movie import format_vote_average

CI_ENV = os.getenv("CI") == "false"

def test_movie_year_min():
    assert format_movie_year_min("1990") == "1990-01-01"
    #assert format_movie_year_min("") == None

def test_vote_average():
    assert format_vote_average("7.2") == 7.2
    assert format_vote_average("") == None
    with pytest.raises(ValueError) as ERROR:
        format_vote_average("seventy") 

def test_runtime_min():
    assert format_runtime_min("100") == 100
    assert format_runtime_min("") == None
    with pytest.raises(ValueError) as ERROR:
        format_runtime_min("one-hundred") 

def test_runtime_max():
    assert format_runtime_max("100") == 100
    assert format_runtime_max("") == None
    with pytest.raises(ValueError) as ERROR:
        format_runtime_max("one-hundred") 

def test_movie_certification():
    assert format_movie_certification("PG") == "PG"
    assert format_movie_certification("") == None

def test_genre_string_to_id():
    assert genre_string_to_id("Animation") == "16"
    assert genre_string_to_id("animation") == "16"
    assert genre_string_to_id("") == None

CI_ENV = os.getenv("CI") == "true"

@pytest.mark.skipif(CI_ENV==True, reason="to avoid issuing HTTP requests on the CI server") # skips this test on CI

def test_run_API():
    assert run_API("two-thousand", None, None, None, None, None, None, None) == None