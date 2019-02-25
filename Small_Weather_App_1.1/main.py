from flask import Flask, render_template, request, redirect, url_for, flash, session
import requests
import json
import os
from weather import query_api
from weather import query_api2
import graf
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from pprint import pprint as pp
import pygal
import pytest

from flask_babel import Babel,gettext

from flask_caching import Cache



from datetime import datetime


app = Flask(__name__)
babel=Babel(app)
app.debug = True
app.secret_key = b'xen_o7q536_*88^j-)m$pyyp*gmq$()8!p*ral@+k5+_=^jnjd'
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
# Prijevod
app.config['BABEL_DEFAULT_LOCALE'] = 'en'



class Logiranje(FlaskForm):
    username=StringField('Username',validators=[DataRequired])
    password=PasswordField('Password',validators=[DataRequired])

# ruta odgovorna za logiranje
@app.route("/login", methods=['GET', 'POST'])
def log():
   
     form=Logiranje()

     error = None

     if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'admin':
            error = 'Invalid username or password. Please try again!'
        else:
            flash('You are successfully logged in', 'success')
            return redirect(url_for('chart'))

     return render_template('login.html', error=error,form =form)

# pocetna ruta,landing page
@app.route("/",methods=['GET', 'POST'])
@app.route("/home",methods=['GET', 'POST'])
def index():

    api_radar=('https://api.sat24.com/animated/EU/visual/1/Central%20European%20Standard%20Time/2793031')
  
   
    
    now =datetime.now()
    now=now.strftime("%Y-%m-%d at %H:%M:%S")
   
    
    return render_template(
        'index.html',now=now,
        data=[{'name': 'Zadar'}, {'name': 'Zagreb'}, {'name': 'Calgary'},
              {'name': 'New York'}, {'name': 'Sydney'}, {
                  'name': 'Moscow'},
              {'name': 'Paris'}, {'name': 'London'}, {
                  'name': 'Brasilia'},
              {'name': 'Shanghai'}])

# prognoza za odabrani grad
@app.route("/result", methods=['POST'])
def result():
    data = []
    data2=[]

    error = None
    select = request.form.get('comp_select')
    
    resp = query_api(select)
    resp2=query_api2(select)
    
    
   
    if resp:
        data.append(resp)
        data2.append(resp2)
    if len(data) != 2:
        error = 'Bad Response from Weather API'

    forecast=(data2[0]['list'])
    return render_template(
        'result.html',
        data=data,
        error=error,data2=data2,forecast=forecast)

#ruta na grafikon
@app.route("/chart")
def chart():

    try:
        worldmap_chart = pygal.maps.world.World()
        worldmap_chart.title = 'Countries where weather data is measured'
        worldmap_chart.add('European countries', ['hr', 'fr', 'gb'])
        worldmap_chart.add('North America countries', ['us', 'ca'])
        worldmap_chart.add('South America countries', ['br'])
        worldmap_chart.add('Australia', ['au'])
        worldmap_chart.add('Asia countries', ['cn'])

        graph_data = worldmap_chart.render_data_uri()

    except Exception as exc:
        print(exc)

    return render_template('chart.html', graph_data=graph_data)


@babel.localeselector
def get_locale():
    if request.args.get('lang'):
        session['lang'] = request.args.get('lang')
    return session.get('lang','en')



if __name__ == "__main__":

    app.run()
