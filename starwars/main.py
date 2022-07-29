import requests

def test_length():
    assert len(get_starships()) == 36

def test_type():
    assert type(get_starships()) == type([])






