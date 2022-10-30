from flask import Blueprint
from flask import Flask
from flask import render_template

bp = Blueprint('main', __name__, template_folder='templates')


@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/event-info')
def event_info():

    return render_template('Event_Info_Page.html')

@bp.route('/event-creation')
def event_creation():

    return render_template('Event_Creation')

@bp.route('Booking_History.html')
def booking_histor():

    return render_template('Booking_History')


@bp.route('/user', methods=['GET', 'POST'])
def user():
    return render_template('user.html')
