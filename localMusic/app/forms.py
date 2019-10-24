from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField, SelectMultipleField
from wtforms.fields.html5 import DateField
from wtforms.validators import ValidationError, DataRequired, EqualTo
from app.models import User



class newArtistForm(FlaskForm):
    artistName = StringField('Artist Name', validators=[DataRequired()])
    hometown = StringField('Home Town', validators=[DataRequired()])
    bio = TextAreaField("Description", validators=[DataRequired()])
    submit = SubmitField('Create New Artist')

class newVenueForm(FlaskForm):
    name = StringField('Venue Name', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    submit = SubmitField('Create New Venue')


class newEventForm(FlaskForm):
    title = StringField('Event Title', validators=[DataRequired()])
    date = DateField('Date and Time', validators=[DataRequired()])
    venue = SelectField('Venue', coerce=int, validators=[DataRequired()])
    artists = SelectMultipleField('Artists', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Create New Event')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email.')

