from flask import Flask, request, Response, render_template, redirect, flash, url_for
import requests
import itertools
from flask_wtf.csrf import CSRFProtect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import wtforms
from wtforms.validators import Regexp
import re

csrf = CSRFProtect()
app = Flask(__name__)
app.config["SECRET_KEY"] = 'RGAPI-9c414491-3eff-467b-a256-7b5599792a19'  
csrf.init_app(app)

@app.route('/')
def default():
    return redirect(url_for('index'))

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/proxy/<summoner_name>')
def proxy(summoner_name):
    result = requests.get(f'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + summoner_name + '?api_key=' + app.config["SECRET_KEY"])
    resp = Response(result.text)
    resp.headers['Content-Type'] = 'application/json'
    return resp