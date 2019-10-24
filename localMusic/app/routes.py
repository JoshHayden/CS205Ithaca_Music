from flask import render_template, flash, redirect, url_for, request
from app import app, db
from flask_wtf import FlaskForm
from random import randrange
from app.forms import *
from app.models import *
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse


@app.route('/')
@app.route('/index')
def index():
    description = "Welcome to Josh's Local Music Emporium, the number one location for all things local music."
    return render_template('index.html', title = "Home", description = description)

@app.route('/listOfArtists')
def listOfArtists():
    list = db.session.query(Artist).all()



    return render_template('listOfArtists.html', title = "List of Artists", artists = list)

@app.route('/createNewArtist', methods = ['GET', 'POST'])
def createNewArtist():
    form = newArtistForm()
    if form.validate_on_submit():
        if (db.session.query(Artist).filter_by(name = form.artistName.data).first()):
            flash("Artist already exists")
            return render_template('createNewArtist.html', title = "Create New Artist", form = form)
        flash('New Artist Created: {}, '.format(
            form.artistName.data))
        artist = Artist(form.artistName.data, form.hometown.data, form.bio.data)
        db.session.add(artist)
        db.session.commit()
        list = db.session.query(Artist).all()

        return render_template('listOfArtists.html', title="List of Artists", artists=list)

    return render_template('createNewArtist.html', title = "Create New Artist", form = form)

@app.route('/createNewVenue', methods = ['GET', 'POST'])
def createNewVenue():
    form = newVenueForm()
    if form.validate_on_submit():
        if (db.session.query(Venue).filter_by(name = form.name.data).first()):
            flash("Venue already exists")
            return render_template('createNewVenue.html', title = "Create New Venue", form = form)
        flash('New Venue Created: {}, '.format(
            form.name.data))
        venue = Venue(form.name.data, form.address.data)
        db.session.add(venue)
        db.session.commit()

        return render_template('index.html', title="Home", description="")

    return render_template('createNewVenue.html', title = "Create New Venue", form = form)

@app.route('/createNewEvent', methods = ['GET', 'POST'])
def createNewEvent():
    artists = db.session.query(Artist).all()
    venues = db.session.query(Venue).all()
    artistList = [(i.id, i.name) for i in artists]
    venueList = [(i.id, i.name) for i in venues]
    form = newEventForm()
    form.artists.choices = artistList
    form.venue.choices = venueList
    if form.validate_on_submit():
        if (db.session.query(Event).filter_by(title = form.title.data).first()):
            flash("Event already exists")
            return render_template('createNewEvent.html', title = "Create New Event", form = form)
        flash('New Event Created: {}, '.format(
            form.title.data))
        event = Event(form.title.data, form.date.data, form.venue.data)
        db.session.add(event)
        db.session.commit()
        eventID = event.id
        for artist in form.artists.data:
            connection = ArtistToEvent(eventID, artist)
            db.session.add(connection)
            db.session.commit()

        return render_template('index.html', title="Home", description="")

    return render_template('createNewEvent.html', title = "Create New Event", form = form)

@app.route('/artist/<name>')
def artist(name):

    artist = db.session.query(Artist).filter_by(name = name).first()
    events = db.session.query(Event).join(ArtistToEvent, ArtistToEvent.eventID == Event.id).join(Artist, Artist.id == ArtistToEvent.artistID).filter(Artist.name == name).all()



    return render_template('artistPage.html', title = name, artist = artist, events = events)



@app.route('/reset_db')
def reset_db():
   flash("Resetting database: deleting old data and repopulating with dummy data")

   meta = db.metadata
   for table in reversed(meta.sorted_tables):
       print('Clear table {}'.format(table))
       db.session.execute(table.delete())
   db.session.commit()
   # now create Artist, Venues, Events, and ArtistToEvent Objects and persist them to the db
   ofMontreal = Artist('of Montreal', 'Athens, Georgia', "of Montreal is an American indie pop band from Athens, Georgia. It was founded by frontman Kevin Barnes in 1996, named after a failed romance between Barnes and a woman \"of Montreal.\" The band is identified as part of the Elephant 6 collective. Throughout its existence, of Montreal's musical style has evolved considerably and drawn inspiration from 1960s psychedelic pop acts.")
   jennyLewis = Artist('Jenny Lewis', 'Las Vegas, Nevada', "Lewis gained prominence in the 1980s as a child actress, appearing in the films Troop Beverly Hills (1989) and The Wizard (1989) and the television series Brooklyn Bridge (1991‚1993). In the mid-1990s, Lewis semi-retired from acting to focus on her musical career, and formed Rilo Kiley in 1998 with fellow former child actor Blake Sennett. Rilo Kiley released four albums before they disbanded in 2014. Lewis has released four solo albums: Rabbit Fur Coat (2006), Acid Tongue (2008), The Voyager (2014) and On the Line (2019). In addition to Rilo Kiley and her solo career, Lewis has been a member of the Postal Service, Jenny & Johnny and Nice As Fuck.")
   builtToSpill = Artist('Built To Spill', 'Boise, Idaho', "Built to Spill is an American indie rock band based in Boise, Idaho. The band has released eight full-length albums. Their most recent, Untethered Moon, was released on April 21, 2015.")
   magicCityHippies = Artist("Magic City Hippies", 'Miami, Florida', "Modern Animal is set to crown Magic City Hippies as one of streaming's ascendant indie bands, while taking their captivating live show to major festivals like Lollapalooza, Bonnaroo, and BottleRock, alongside plenty of North American headline gigs through 2020.")
   rainbowKitten = Artist('Rainbow Kitten Surprise', 'Boone, North Carolina', "Rainbow Kitten Surprise is an alternative rock indie band, featuring lead vocalist Sam Melo, Darrick “Bozzy” Keller (guitar, backup vocals), Ethan Goodpaster (electric guitar), Jess Haney (drums), and Charlie Holt (bass). Members hail from Boone, North Carolina as well as Robbinsville, North Carolina (Jess Haney and Ethan Goodpaster). The music of Rainbow Kitten Surprise, also known as “RKS,” is known for its harmonies, instrumentation and lyrics, and its sound has been influenced by artists Modest Mouse, Kings of Leon, Frank Ocean and Schoolboy Q.")
   db.session.add(ofMontreal)
   db.session.add(jennyLewis)
   db.session.add(builtToSpill)
   db.session.add(magicCityHippies)
   db.session.add(rainbowKitten)
   #Events
   OMAtHaunt = Event('of Montreal at The Haunt', datetime(2019, 10, 3, 18, 30), 1)
   JLAtState = Event('Jenny Lewis at The State', datetime(2019, 4, 19, 19), 2)
   doubleFeature = Event('MCH and RKS at the Haunt', datetime(2020, 1, 5, 20, 30), 1)
   BTSAtHaunt = Event('Built To Spill at The Haunt', datetime(2019, 12, 13, 17, 30), 1)
   BTSAtState = Event('Built To Spill at The State', datetime(2019, 11, 14, 18, 30), 2)
   RKSAtState = Event('Rainbow Kitten Surprise at The State', datetime(2019, 11, 18, 20), 2)
   db.session.add(OMAtHaunt)
   db.session.add(JLAtState)
   db.session.add(doubleFeature)
   db.session.add(BTSAtHaunt)
   db.session.add(BTSAtState)
   db.session.add(RKSAtState)
   #Venues
   haunt = Venue("The Haunt", '702 Willow Ave, Ithaca, NY, 14850')
   state = Venue("Ithaca State Theater", "107 W State St, Ithaca, NY, 14850")
   db.session.add(haunt)
   db.session.add(state)
   #artistToEvent
   r1 = ArtistToEvent(1, 1)
   r2 = ArtistToEvent(2, 2)
   r3 = ArtistToEvent(3, 4)
   r4 = ArtistToEvent(3, 5)
   r5 = ArtistToEvent(4, 3)
   r6 = ArtistToEvent(5, 3)
   r7 = ArtistToEvent(6, 5)
   db.session.add(r1)
   db.session.add(r2)
   db.session.add(r3)
   db.session.add(r4)
   db.session.add(r5)
   db.session.add(r6)
   db.session.add(r7)
   db.session.commit()
   return render_template('index.html', title="Home", description="Welcome to Josh's Local Music Emporium, the number one location for all things local music.")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email = form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

