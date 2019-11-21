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
app.config["SECRET_KEY"] = 'RGAPI-46336dee-2590-441c-be36-b0dfcce868ec'  
csrf.init_app(app)

@app.route('/proxy/<summoner_name>')
def proxy(summoner_name):
    result = requests.get(f'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + summoner_name + '?api_key=' + app.config["SECRET_KEY"])
    resp = Response(result.text)
    resp.headers['Content-Type'] = 'application/json'
    return resp