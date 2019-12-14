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
from models import LoginForm, SignupForm, ChampionForm
from flask_sqlalchemy import SQLAlchemy

csrf = CSRFProtect()
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///League.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
app.config["SECRET_KEY"] = 'RGAPI-61561ff9-ab11-489e-8ae2-492d6786185d'
# csrf.init_app(app)
# engine
Bootstrap(app)


# favs = db.Table('favs',
#     db.Column('champion_id', db.Integer, db.ForeignKey('champion.champion_id')),
#     db.Column('user_id', db.Integer, db.ForeignKey("user.user_id"))
# )

# class Favs(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     db.Column('champion_id', db.Integer, db.ForeignKey('champion.champion_id'))
#     db.Column('user_id', db.Integer, db.ForeignKey("user.user_id"))




# class Champion(db.Model):
#     champion_id = db.Column(db.Integer, primary_key=True)
#     champion_name = db.Column(db.String(80))
#     # summoner_name = db.Column(db.String(80))
#     favorites = db.relationship('User', secondary='favs', backref=db.backref('following', lazy='dynamic'))

# class User(db.Model):
#     user_id = db.Column(db.Integer, primary_key=True)
#     summoner = db.Column(db.String(80), unique=True)
#     email = db.Column(db.String(120), unique=True)
#     password = db.Column(db.String(120))


#     def __init__(self, summoner, email, password):
#         self.summoner = summoner
#         self.email = email
#         self.password = password

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    summoner_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    Favorites = db.relationship('Champion', backref='user', lazy=True)

    def __init__(self, username, email, password):
        self.summoner_name = username
        self.email = email
        self.password = password

class Champion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    champion_name = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)

db.create_all()
auth = False
summoner_name = ""

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
    global summoner_name
    form = LoginForm(request.form)

    if not form.validate_on_submit():
        return render_template('login.html', form=form)
    if request.method == 'POST':
        # Storing the Logged in user
        user = User.query.filter_by(email=form.email_addr.data).first()

        # If no user is found, then they might have entered the wrong credentials
        # If the user entered the correct username, but the wrong password, error is shown
        if user is None:
            return render_template('login.html', form=form, message="Incorrect Username or Password")
        elif user.password == form.password.data:   
            # Confirming the user logged in
            auth = True
            summoner_name = user.summoner_name
            print(summoner_name)
            return render_template('index.html', form=form, loggedin=auth)
        else:
            return render_template('login.html', form=form, message="Incorrect Password", loggedin=auth)

@app.route('/logout')
def logout():
    global auth
    global summoner_name
    auth = False
    summoner_name = ""
    return render_template("index.html", loggedin=auth)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    global auth
    form = SignupForm(request.form)
    if not form.validate_on_submit():
        return render_template('signup.html', form=form)
    if request.method == 'POST':

        userEmail = User.query.filter_by(email=form.email_addr.data).first()
        userSummoner = User.query.filter_by(summoner_name=form.summoner.data).first()

        if userEmail is not None:
            return render_template('signup.html', form=form, message="Email already exists.", loggedin=auth)
        
        if userSummoner is not None:
            return render_template('signup.html', form=form, message="Summoner already exists.", loggedin=auth)

        if not summonerExists(form.summoner.data):
            return render_template('signup.html', form=form, message="Summoner Name does not exist.", loggedin=auth)

        user = User(form.summoner.data, form.email_addr.data, form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))

def summonerExists(summoner_name):
    region = "na1"
    result = requests.get('https://' + region + '.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + summoner_name + '?api_key=' + app.config["SECRET_KEY"])
    json_data = result.json()
    try:
        if (json_data["status"]["message"]) == "Data not found - summoner not found":
            return False
    except:
        return True

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

@app.route('/champions', methods=['GET', 'POST'])
def champions():
    global auth
    global summoner_name

    # Getting Logged In user.
    loggedInuser = User.query.filter_by(summoner_name=summoner_name).first()

    champion_ls = ['Qiyana', 'Wukong', 'Jax', 'Kayn', 'Yuumi', 'Shaco', 'Warwick', 'Xayah', 'Sylas', 'Nidalee', 'Zyra', 'Kled', 'Brand', 'Rammus', 'Illaoi', 'Corki', 'Braum', 'Darius', 'Tryndamere', 'MissFortune', 'Yorick', 'Xerath', 'Sivir', 'Riven', 'Orianna', 'Sejuani', 'Gangplank', 'Malphite', 'Poppy', 'Kaisa', 'Jayce', 'Blitzcrank', 'Trundle', 'Karthus', 'Zoe', 'Graves', 'Lucian', 'Nocturne', 'Lux', 'Shyvana', 'Renekton', 'Fiora', 'Jinx', 'Kalista', 'Fizz', 'Kassadin', 'Sona', 'Vladimir', 'Viktor', 'Rakan', 'Kindred', 'Cassiopeia', 'Maokai', 'Ornn', 'Thresh', 'Kayle', 'Hecarim', 'Khazix', 'Olaf', 'Ziggs', 'Syndra', 'DrMundo', 'Karma', 'Annie', 'Akali', 'Leona', 'Yasuo', 'Kennen', 'Rengar', 'Ryze', 'Shen', 'Zac', 'Pantheon', 'Neeko', 'Bard', 'Sion', 'Vayne', 'Nasus', 'Fiddlesticks', 'TwistedFate', 'Chogath', 'Udyr', 'Morgana', 'Ivern', 'Volibear', 'Caitlyn', 'Anivia', 'Gnar', 'Rumble', 'Zilean', 'Azir', 'Diana', 'Skarner', 'Teemo', 'Urgot', 'Amumu', 'Galio', 'Heimerdinger', 'Ashe', 'Velkoz', 'Singed', 'Taliyah', 'Senna', 'Varus', 'Twitch', 'Garen', 'Nunu', 'MasterYi', 'Pyke', 'Elise', 'Alistar', 'Katarina', 'Ekko', 'Mordekaiser', 'KogMaw', 'Camille', 'Aatrox', 'Draven', 'TahmKench', 'Talon', 'XinZhao', 'Swain', 'AurelionSol', 'LeeSin', 'Aphelios', 'Taric', 'Malzahar', 'Lissandra', 'Tristana', 'RekSai', 'Irelia', 'JarvanIV', 'Nami', 'Jhin', 'Soraka', 'Veigar', 'Janna', 'Nautilus', 'Evelynn', 'Gragas', 'Zed', 'Vi', 'Lulu', 'Ahri', 'Quinn', 'Leblanc', 'Ezreal']
    
    form = ChampionForm(request.form)
    if not form.validate_on_submit():
        return render_template('champions.html', form=form, loggedin= auth)
    if request.method == 'POST':
        championExistsInDataBase = False
        for champion in loggedInuser.Favorites:
            if form.add_champion.data == champion.champion_name:
                championExistsInDataBase = True
        
        if championExistsInDataBase:
            return render_template('champions.html', form=form, loggedin= auth, message = "Champion already added.")
        if form.add_champion.data not in champion_ls:
            return render_template('champions.html', form=form, loggedin= auth, message = "Champion does not exists.")

        champion = Champion(champion_name=form.add_champion.data, user_id=loggedInuser.id)
        db.session.add(champion)
        db.session.commit()

        return render_template('champions.html', form=form, loggedin= auth,)

    

    # return render_template("champions.html", loggedin=auth)

@app.route('/proxy/<region>/<summoner_name>')
def proxy(region, summoner_name):
    #First request to get id
    result = requests.get('https://' + region + '.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + summoner_name + '?api_key=' + app.config["SECRET_KEY"])
    json_data = result.json()

    try:
        account_id = json_data['id']

        #Second request to get account data
        url = 'https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/' + account_id + '?api_key=' + app.config["SECRET_KEY"]
        result = requests.get(url)
        resp = Response(result.text)
        resp.headers['Content-Type'] = 'application/json'
        return resp
    
    except:
        resp = Response()
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

@app.route('/proxy/champions')
def proxychampions():
    region = "na1"
    #First request to get id
    result = requests.get('https://' + region + '.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + summoner_name + '?api_key=' + app.config["SECRET_KEY"])
    json_data = result.json()
    account_id = json_data['id']

    #Second request to get account data
    url = 'https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/' + account_id + '?api_key=' + app.config["SECRET_KEY"]
    result = requests.get(url)
    resp = Response(result.text)
    resp.headers['Content-Type'] = 'application/json'
    return resp