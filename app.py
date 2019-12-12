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

@app.route('/news')
def news():
    return render_template("news.html")

@app.route('/leaderboard')
def leaderboard():
    return render_template("leaderboard.html")

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

@app.route('/proxy/news/<type>')
def proxynews(type):
    url = 'https://newsapi.org/v2/everything?' + 'q=' + type + '&' + 'pageSize=100&' + 'apiKey=b1af8f73115e4ced9713842b854e198e'
    result = requests.get(url)
    resp = Response(result.text)
    resp.headers['Content-Type'] = 'application/json'
    return resp

@app.route('/proxy/challenger')
def proxychallenger():
    url = 'https://na1.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5?api_key=' + app.config["SECRET_KEY"]
    result = requests.get(url)
    resp = Response(result.text)
    resp.headers['Content-Type'] = 'application/json'
    return resp