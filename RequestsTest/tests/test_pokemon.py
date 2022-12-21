import requests
import pytest


def test_status_code():
    response = requests.get('https://pokemonbattle.me:5000/trainers')
    assert response.status_code == 200

def test_piece_of_body():
    response = requests.get('https://pokemonbattle.me:5000/trainers', params={'trainer_id' : 'your id'})
    assert response.json()['trainer_name'] == 'your name'

@pytest.mark.parametrize('key, value', [('trainer_name','your name'),('city','your city')])

def test_parametrs_body(key, value):
    response = requests.get('https://pokemonbattle.me:5000/trainers', params={'trainer_id' : 'your id'})
    assert response.json()[key] == value










