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
from flask_bootstrap import Bootstrap
from models import LoginForm, SignupForm
from flask_sqlalchemy import SQLAlchemy

csrf = CSRFProtect()
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
app.config["SECRET_KEY"] = 'RGAPI-61561ff9-ab11-489e-8ae2-492d6786185d'
# csrf.init_app(app)

Bootstrap(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120), unique=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username

db.create_all()
auth = False

@app.route('/')
def default():
    return redirect(url_for('index'))

@app.route('/index')
def index():
    global auth
    return render_template("index.html", loggedin=auth)

@app.route('/login', methods=['GET', 'POST'])
def login():
    global auth
    form = LoginForm(request.form)

    if not form.validate_on_submit():
        return render_template('login.html', form=form)
    if request.method == 'POST':
        user = User.query.filter_by(email=form.email_addr.data).first()
        if user is None:
            return render_template('login.html', form=form, message="Incorrect Username or Password")
        elif user.password == form.password.data:
            auth = True
            return render_template('index.html', form=form, loggedin=auth)
        else:
            return render_template('login.html', form=form, message="Incorrect Password", loggedin=auth)

@app.route('/logout')
def logout():
    global auth
    auth = False
    return render_template("index.html", loggedin=auth)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    global auth
    form = SignupForm(request.form)
    if not form.validate_on_submit():
        return render_template('signup.html', form=form)
    if request.method == 'POST':

        userEmail = User.query.filter_by(email=form.email_addr.data).first()
        userSummoner = User.query.filter_by(username=form.summoner.data).first()

        if userEmail is not None:
            return render_template('signup.html', form=form, message="Email already Exists", loggedin=auth)
        
        if userSummoner is not None:
            return render_template('signup.html', form=form, message="Summoner already Exists", loggedin=auth)
        user = User(form.summoner.data, form.email_addr.data, form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))

@app.route('/news')
def news():
    global auth
    return render_template("news.html", loggedin=auth)

@app.route('/leaderboard')
def leaderboard():
    global auth
    return render_template("leaderboard.html", loggedin=auth)

@app.route('/rotation')
def rotation():
    global auth
    return render_template("rotation.html", loggedin=auth)

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

@app.route('/proxy/rotation')
def proxyrotation():
    url = 'https://na1.api.riotgames.com/lol/platform/v3/champion-rotations?api_key=' + app.config["SECRET_KEY"]
    result = requests.get(url)
    resp = Response(result.text)
    resp.headers['Content-Type'] = 'application/json'
    return resp