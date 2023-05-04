from flask import Blueprint, render_template, jsonify, request
from requests import get

pokebp = Blueprint('pokedex', __name__)

@pokebp.route('/pokedex')
def pokemons():
    content = get ('https://studies.delpech.info/pbi/pokemons/dataset/json')
    pokemons = content.json()
    return render_template('pokedex.jinja', pokemons=pokemons)

@pokebp.route('/pokemon/<int:id>')
def pokemon(id):
    url = 'https://studies.delpech.info/pbi/pokemons/dataset/{}/json'.format(id)
    pokemon = get(url).json()
    pokemon_id = int(url.split('/dataset/')[1].split('/json')[0])
    return render_template('pokemon.jinja', pokemon=pokemon, pokemon_id=pokemon_id)
