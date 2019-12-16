from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import Length, Email, InputRequired, DataRequired, EqualTo

# Form ORM
class LoginForm(FlaskForm):
        email_addr = TextField('', validators=[InputRequired(), Email()])
        password = PasswordField('', validators=[DataRequired()])
        submit = SubmitField('Submit')

# Form ORM
class SignupForm(FlaskForm):
        email_addr = TextField('', validators=[InputRequired(), Email()])
        summoner = TextField('', validators=[InputRequired()])
        password = PasswordField('', validators=[DataRequired(), EqualTo('confirm', message='Passwords must match')])
        confirm = PasswordField('')
        submit = SubmitField('Submit')

class ChampionForm(FlaskForm):
        add_champion = TextField('', validators=[InputRequired()])
        add_btn = SubmitField(label='Add', id="submitBtn")
        remove_btn = SubmitField(label='Remove', id="submitBtn")

class PlayerForm(FlaskForm):
        add_player = TextField('', validators=[InputRequired()])
        add_btn = SubmitField(label='Add', id="submitBtn")
        remove_btn = SubmitField(label='Remove', id="submitBtn")

class SpellForm(FlaskForm):
        add_spell = TextField('', validators=[InputRequired()])
        add_btn = SubmitField(label='Add', id="submitBtn")
        remove_btn = SubmitField(label='Remove', id="submitBtn")