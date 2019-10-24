from datetime import datetime
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash




class Artist(db.Model):
    __tablename__ = 'Artist'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    hometown = db.Column(db.String(64), index=True)
    bio = db.Column(db.String(1024))

    def __repr__(self):
        return '<Artist {}>'.format(self.name)

    def __init__(self, enteredName, enteredHometown, enteredBio):
        self.name = enteredName
        self.hometown = enteredHometown
        self.bio = enteredBio

class Venue(db.Model):
    __tablename__ = 'Venue'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    address = db.Column(db.String(128), index=True)
    events = db.relationship('Event', backref='venue', lazy='dynamic')

    def __repr__(self):
        return '<Venue {}>'.format(self.name)

    def __init__(self, name, address):
        self.name = name
        self.address = address

class Event(db.Model):
    __tablename__ = 'Event'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True)
    date = db.Column(db.DateTime, index=True)
    venueID = db.Column(db.Integer, db.ForeignKey('Venue.id'))

    def __repr__(self):
        return '<Event {}>'.format(self.title)

    def __init__(self, title, date, venueID):
        self.title = title
        self.date = date
        self.venueID = venueID

class ArtistToEvent(db.Model):
    __tablename__ = 'ArtistToEvent'
    id = db.Column(db.Integer, primary_key=True)
    eventID = db.Column(db.Integer, db.ForeignKey('Event.id'))
    artistID = db.Column(db.Integer, db.ForeignKey('Artist.id'))

    def __repr__(self):
        return '<ArtistToEvent {}>'.format(self.id)

    def __init__(self, eventID, artistID):
        self.eventID = eventID
        self.artistID = artistID


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(64), index = True, unique = True)

    def __repr__(self):
        return '<User {}>'.format(self.username)


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def user_loader(id):
    return User.query.get(int(id))