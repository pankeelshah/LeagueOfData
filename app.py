from flask import Flask, request, Response, render_template, redirect, flash, url_for
import requests
import itertools
from flask_wtf.csrf import CSRFProtect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import wtforms
from wtforms.validators import Regexp
import re
import json

csrf = CSRFProtect()
app = Flask(__name__)
app.config["SECRET_KEY"] = 'RGAPI-61561ff9-ab11-489e-8ae2-492d6786185d'  
csrf.init_app(app)

@app.route('/')
def default():
    return redirect(url_for('index'))

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/proxy/<region>/<summoner_name>')
def proxy(region, summoner_name):
    #First request to get id
    result = requests.get('https://' + region + '.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + summoner_name + '?api_key=' + app.config["SECRET_KEY"])
    json_data = result.json()
    account_id = json_data['id']

    #Second request to get account data
    url = 'https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/' + account_id + '?api_key=' + app.config["SECRET_KEY"]
    result = requests.get(url)
    resp = Response(result.text)
    resp.headers['Content-Type'] = 'application/json'
    return resp