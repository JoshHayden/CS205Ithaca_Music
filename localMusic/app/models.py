from datetime import datetime
from app import db



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


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), index=True, unique=True)
#     email = db.Column(db.String(120), index=True, unique=True)
#     password_hash = db.Column(db.String(128))
#     posts = db.relationship('Post', backref='author', lazy='dynamic')
#
#     def __repr__(self):
#         return '<User {}>'.format(self.username)
#
#
# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     body = db.Column(db.String(140))
#     timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#
#     def __repr__(self):
#         return '<Post {}>'.format(self.body)
