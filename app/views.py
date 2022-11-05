from flask import Blueprint, request, flash, redirect, render_template
from flask import Flask
from app.models import Event, Comment, User, ticketOrder
from flask_login import login_required, current_user
from .forms import FindEventForm, CreateEventForm, BuyTicket
from .auth import session
from . import db
from sqlalchemy.orm.attributes import flag_modified
 
 # Create a blueprint
bp = Blueprint('main', __name__, template_folder='templates')


@bp.route('/')
@bp.route('/index')
def index():
    #Get list of all events
    allEvent = Event.query.all()
    return render_template('index.html', allEvent=allEvent)


# If users get a 404 or 500 error load the corressponding error page
@bp.errorhandler(404)
def page_not_found():
    return render_template('404.html')

@bp.errorhandler(500)
def page_not_found():
    return render_template('500.html')


#@bp.route('/event_info_page', methods=['GET', 'POST'])
#def event_info_page():
#    def get_choices():
#        return Event.query.order_by(Event.eventName)
#
#    form = FindEventForm()
#    choices = get_choices
#    form.event_id.choices = choices
#    
#    if form.validate_on_submit():
#        event = Event.query.filter_by(eventName=form.data).first()
#        event_id = event.id
#        event_user = event.userId
#        event_name = event.eventName
#        event_date = event.eventDate
#        event_t_type = event.ticketTypes
#        event_desc = event.description
#        event_stat = event.eventStatus
#        event_comments = event.comments
#        event_orders = event.ticketOrders
#    return render_template('event_info_page.html', form=form)


@bp.route('/event_creation', methods=['GET', 'POST'])
def event_creation():
    if current_user.is_authenticated:
        form = CreateEventForm()
        if form.validate_on_submit():
            file = request.files['file']
            # If input data meets all validators and user is logged in send
            # all new event data to a database
            event = Event(
                creatorUserId = session['UserID'],
                eventName = form.event_name.data,
                eventDate = form.event_date.data,
                eventTime = form.event_time.data,
                description = form.event_description.data,
                ticketPrice = form.ticket_price.data,
                numberOfTickets = form.number_of_tickets.data,
                eventStatus = form.event_status.data,
                eventImg = file.read()
            )
            db.session.add(event)
            db.session.commit()
            return redirect('/index')
    else:
        flash('Not logged in')
        return redirect('/login')
    return render_template('event_creation.html', title = 'EVENT_CREATION', form=form)



#@bp.route('/booking_history', methods=['GET', 'POST'])
#def booking_history():
#    bookings = []
#    if "UserID" in session:
#        tickets = ticketOrder.query.filter_by(session['UserID']).all()
#        for ticket in tickets:
#            bookings.append(ticket)
#    else:
#        flash('Not logged in')
#        return redirect('/login')
#    return render_template('booking_history.html', **locals())



@bp.route('/my_events', methods=['GET', 'POST'])
def my_events():
    # Check user is logged in, and if so fetch all event data from the database
    # that matches with their user id
    if current_user.is_authenticated:
        myName = User.query.filter_by(id=current_user.id)
        myEvent = Event.query.filter_by(creatorUserId=current_user.id).all()
    else:
        flash('Not logged in')
        return redirect('/login')
    return render_template("my_events.html", myName=myName, myEvent=myEvent)


# Create dynamic url to fetch details on any event
@bp.route('/event/<int:eventId>', methods=['GET', 'POST'])
def event(eventId):
    form=BuyTicket()
    chosenEvent = Event.query.filter_by(id=eventId)
    return render_template("event_info_page.html", chosenEvent=chosenEvent, form=form)