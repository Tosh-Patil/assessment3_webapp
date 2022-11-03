from flask import Blueprint, request
from flask import Flask
from flask import render_template
from website.models import Event, Comment

bp = Blueprint('main', __name__, template_folder='templates')


@bp.route('/')
@bp.route('/index')
def index():
    #Get list of events
    event = Event.query.order_by(Event.eventName)


    return render_template('index.html', **locals())

@bp.route('/event_info', methods=['GET', 'POST'])
def event_info(event_id):

    event = Event.query.get(event_id)
    event_name = Event.eventName
    event_info = Event.description
    event_date = Event.eventDate
    event_ticket_types = Event.ticketTypes
    event_status = Event.eventStatus

    comments = Comment.query.filter_by(eventId = event_id).all()

    if request.method == 'POST':
        #Booking tickets backend here
        pass

    return render_template('event_info_page.html', event=event, event_name=event_name, event_info=event_info, event_date=event_date, 
    event_ticket_types=event_ticket_types, event_status=event_status, **locals())

@bp.route('/event_creation', methods=['GET', 'POST'])
def event_creation():

    if request.method == 'POST':
        #creating an event backend here
        pass

    return render_template('event_creation.html')

@bp.route('/booking_history', methods=['GET', 'POST'])
def booking_history():
    # tickets = ticketOrder.query.query_by(USERID)

    return render_template('booking_history.html', **locals())


@bp.route('/user', methods=['GET', 'POST'])
def user():

    return render_template('user.html')
