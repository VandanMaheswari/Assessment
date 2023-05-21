import requests

url = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"

response = requests.get(url)

if response.status_code == 200:
    print("The URL is working.")
else:
    print("Failed to retrieve data. Status code:", response.status_code)
