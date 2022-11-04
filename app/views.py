from flask import Blueprint, request
from flask import Flask
from flask import render_template
from app.models import Event, Comment
from flask_login import login_required
from .forms import FindEventForm
 
bp = Blueprint('main', __name__, template_folder='templates')


@bp.route('/')
@bp.route('/index')
def index():
    #Get list of events
    event = Event.query.order_by(Event.eventName)


    return render_template('index.html', **locals())

@bp.route('/event_info_page', methods=['GET', 'POST'])
def event_info_page():
    
    def get_choices():
        return Event.query.order_by(Event.eventName)

    form = FindEventForm()
    choices = get_choices
    form.event_id.choices = choices
    
    if form.validate_on_submit:
        event_name = form.event_id

    return render_template('event_info_page.html', form=form, event_name=event_name)

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
@login_required
def user():

    return render_template('user.html')
