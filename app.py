from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import date
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rsvp.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class RSVP(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    plus_ones = db.Column(db.Integer, default=0)

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

@app.route('/rsvp', methods=['GET', 'POST'])
def rsvp():
    if request.method == 'POST':
        name = request.form['name']
        plus_ones = int(request.form['plus_ones'])
        rsvp_entry = RSVP(name=name, plus_ones=plus_ones)
        db.session.add(rsvp_entry)
        db.session.commit()
        return redirect(url_for('rsvp_list'))
    return render_template('rsvp.html')

@app.route('/rsvp-list')
def rsvp_list():
    rsvps = RSVP.query.all()
    total_guests = sum(rsvp.plus_ones + 1 for rsvp in rsvps)  # Counting each RSVP plus one
    return render_template('rsvp_list.html', rsvps=rsvps, total_guests=total_guests)

@app.route('/travel-and-stay')
def travel_and_stay():
	return render_template('travel-and-stay.html')