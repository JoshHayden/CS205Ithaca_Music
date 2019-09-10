from flask import render_template
from app import app
from random import randrange


@app.route('/')
@app.route('/index')
def index():
    description = "Welcome to Josh's Local Music Emporium, the number one location for all things local music."
    return render_template('index.html', title = "Home", description = description)
@app.route('/listOfArtists')
def listOfArtists():
    list = [{"artistName":"of Montreal",
             'bio': 'of Montreal is an American indie pop band from Athens, Georgia. It was founded by frontman Kevin Barnes in 1996, named after a failed romance between Barnes and a woman "of Montreal." The band is identified as part of the Elephant 6 collective. Throughout its existence, of Montreal\'s musical style has evolved considerably and drawn inspiration from 1960s psychedelic pop acts.',
        'hometown':"Athens, Georgia", 'events': ['September 24th at the Haunt', 'December 16th at the A&E center'], 'pageLocation':'/ofMontreal'},
            {"artistName": "Jenny Lewis",
             'bio': 'of Montreal is an American indie pop band from Athens, Georgia. It was founded by frontman Kevin Barnes in 1996, named after a failed romance between Barnes and a woman "of Montreal." The band is identified as part of the Elephant 6 collective. Throughout its existence, of Montreal\'s musical style has evolved considerably and drawn inspiration from 1960s psychedelic pop acts.',
             'hometown': "Athens, Georgia",
             'events': ['September 24th at the Haunt', 'December 16th at the A&E center'],
             'pageLocation': '/ofMontreal'},
            {"artistName": "Built To Spill",
             'bio': 'of Montreal is an American indie pop band from Athens, Georgia. It was founded by frontman Kevin Barnes in 1996, named after a failed romance between Barnes and a woman "of Montreal." The band is identified as part of the Elephant 6 collective. Throughout its existence, of Montreal\'s musical style has evolved considerably and drawn inspiration from 1960s psychedelic pop acts.',
             'hometown': "Athens, Georgia",
             'events': ['September 24th at the Haunt', 'December 16th at the A&E center'],
             'pageLocation': '/ofMontreal'},
            {"artistName": "Magic City Hippies",
             'bio': 'of Montreal is an American indie pop band from Athens, Georgia. It was founded by frontman Kevin Barnes in 1996, named after a failed romance between Barnes and a woman "of Montreal." The band is identified as part of the Elephant 6 collective. Throughout its existence, of Montreal\'s musical style has evolved considerably and drawn inspiration from 1960s psychedelic pop acts.',
             'hometown': "Athens, Georgia",
             'events': ['September 24th at the Haunt', 'December 16th at the A&E center'],
             'pageLocation': '/ofMontreal'},
            {"artistName": "Rainbow Kitten Surprise",
             'bio': 'of Montreal is an American indie pop band from Athens, Georgia. It was founded by frontman Kevin Barnes in 1996, named after a failed romance between Barnes and a woman "of Montreal." The band is identified as part of the Elephant 6 collective. Throughout its existence, of Montreal\'s musical style has evolved considerably and drawn inspiration from 1960s psychedelic pop acts.',
             'hometown': "Athens, Georgia",
             'events': ['September 24th at the Haunt', 'December 16th at the A&E center'],
             'pageLocation': '/ofMontreal'}]

    return render_template('listOfArtists.html', title = "List of Artists", artists = list)

@app.route('/createNewArtist')
def createNewArtist():
    return render_template('createNewArtist.html', title = "Add New Artist", description = "Placeholder for now.")

@app.route('/ofMontreal')
def ofMontreal():
    artist = {"artistName":"of Montreal",
             'bio': 'of Montreal is an American indie pop band from Athens, Georgia. It was founded by frontman Kevin Barnes in 1996, named after a failed romance between Barnes and a woman "of Montreal." The band is identified as part of the Elephant 6 collective. Throughout its existence, of Montreal\'s musical style has evolved considerably and drawn inspiration from 1960s psychedelic pop acts.',
        'hometown':"Athens, Georgia", 'events': ['September 24th at the Haunt', 'December 16th at the A&E center'], 'pageLocation':'/ofMontreal'}
    return render_template('artistPage.html', title = 'of Montreal', artist = artist)