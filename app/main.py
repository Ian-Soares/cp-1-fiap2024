from fastapi import FastAPI
import datetime
import requests

app = FastAPI(title="Cloud developer - CP1")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/get_pokemon_data/{pokemon}")
def read_cp1(pokemon: str):
    r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
    return {
        "Name": f"{r.json()['name']}",
        "Abilities": f"{[r.json()['abilities'][x]['ability']['name'] for x in range(len(r.json()['abilities']))]}",
        "Height": f"{int(r.json()['height'])*10} cm",
        "Weight": f"{r.json()['weight']/10} kg"
        }