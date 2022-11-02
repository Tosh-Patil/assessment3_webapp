from flask import Blueprint, request
from flask import Flask
from flask import render_template
from website.models import Event, Comment

bp = Blueprint('main', __name__, template_folder='templates')


@bp.route('/')
def index():
    #Get list of events
    event = Event.query.order_by(Event.eventName)


    return render_template('index.html', **locals())

@bp.route('/event-info', methods=['GET', 'POST'])
def event_info(event_id):

    event = Event.query.get(event_id)
    event_name = event.eventName
    event_info = event.description
    event_date = event.eventDate
    event_ticket_types = event.ticketTypes
    event_status = event.eventStatus

    comments = Comment.query.filter_by(eventId = event_id).all()

    if request.method == 'POST':
        #Booking tickets backend here
        pass

    return render_template('Event_Info_Page.html', **locals())

@bp.route('/event-creation', methods=['GET', 'POST'])
def event_creation():

    if request.method == 'POST':
        #creating an event backend here
        pass

    return render_template('Event_Creation.html')

@bp.route('/booking_history', methods=['GET', 'POST'])
def booking_history():
    # tickets = ticketOrder.query.query_by(USERID)

    return render_template('Booking_History.html', **locals())


@bp.route('/user', methods=['GET', 'POST'])
def user():
    
    return render_template('user.html')
