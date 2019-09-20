from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class newArtistForm(FlaskForm):
    artistName = StringField('Artist Name')
    hometown = StringField('Home Town')
    bio = TextAreaField("Description")
    submit = SubmitField('Create New Artist')