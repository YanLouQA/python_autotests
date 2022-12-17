import requests
import json

token = '6c16eccd3e90179dd3dd3c2142ddf0cf'

response = requests.post('https://pokemonbattle.me:5000/pokemons', headers = {'trainer_token' : token}, json={
"name": "Слоубробро",
"photo": "https://projectpokemon.org/home/uploads/monthly_2017_11/59fc44b239ff8_large.GlobalLink.png.42583f82e94967e13ea22482177d2672.png"
})

print(response.text)

response_put = requests.put('https://pokemonbattle.me:5000/pokemons', headers = {'trainer_token' : token}, json={
"pokemon_id": 1948,
"name": "Слоубро",
"photo": ""
})

print(response_put.text)


response_post = requests.post('https://pokemonbattle.me:5000/trainers/addPokebol', headers = {'trainer_token' : token}, json={
"pokemon_id": 1948,
})

print(response_post.text)