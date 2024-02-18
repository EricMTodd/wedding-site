from flask import Flask, render_template
from datetime import date
import os

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
	image_folder = os.path.join(app.static_folder, 'images', 'gallery')
	image_files = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder,f))]
	return render_template('gallery.html', image_files=image_files)

@app.route('/rsvp')
def rsvp():
	return render_template('rsvp.html')

@app.route('/travel-and-stay')
def travel_and_stay():
	return render_template('travel-and-stay.html')