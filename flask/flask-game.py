from flask import Flask, render_template
from random import randrange, uniform


app = Flask(__name__)


@app.route('/')
def huvudmeny():
    return(render_template('meny.html', spelsamling.keys()))

@app.route('/g/string:spelnamn')
def starta_spel(spelnamn):
    return(render_template('spel.html', speldata)

@app.route('/skapa_spelare')
def skapa_spelare()
    return(render_template('skapa_spelare.html')

@app.route('/s/string:spelarnamn')
def visa_spelardata(spelarnamn):
    return(render_template('visa_spelardata.html')


