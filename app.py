from flask import Flask, Blueprint, render_template, jsonify, redirect
from http import HTTPStatus

app = Flask(__name__)

from blueprints.pokebp import pokebp

app.register_blueprint(pokebp)

@app.route('/')
def index():
    return redirect('/pokedex', code=HTTPStatus.FOUND)