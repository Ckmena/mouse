from flask import Flask, render_template
from flask_pymongo import PyMongo
import json
import requests
from datetime import datetime
import pytz

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://admin:123@mongo:27017/charts'
mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/bar-chart')
def bar_chart():
    return render_template('barchart.html')

@app.route('/line-chart')
def line_chart():
    return render_template('linechart.html')

@app.route('/pie-chart')
def pie_chart():
    return render_template('piechart.html')

@app.route('/bubble-chart')
def bubble_chart():
    return render_template('bubblechart.html')


