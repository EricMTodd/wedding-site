from flask import Flask, render_template
from datetime import date

app = Flask(__name__)

@app.route('/')
def index():
	today = date.today()
	event = date(2024, 9, 14)
	delta = event - today
	return render_template('index.html', delta=delta)

@app.route('/event-details')
def event_details():
	return render_template('event-details.html')

@app.route('/gallery')
def gallery():
	return render_template('gallery.html')

@app.route('/rsvp')
def rsvp():
	return render_template('rsvp.html')

@app.route('/travel-and-stay')
def travel_and_stay():
	return render_template('travel-and-stay.html')