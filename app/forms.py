
from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField,SubmitField, StringField, PasswordField, BooleanField, SelectField, TimeField
from wtforms.validators import InputRequired, Length, Email, EqualTo, ValidationError
from flask_wtf.file import FileRequired, FileField, FileAllowed
from .models import User, Event
from . import db

ALLOWED_FILE = {'.PNG','.JPG','.png','.jpg'}

#creates the login information
class LoginForm(FlaskForm):
    username=StringField("Username", validators=[InputRequired('Enter username')])
    password=PasswordField("Password", validators=[InputRequired('Enter password')])
    # Remember me button so user stays logged in
    rememberMe = BooleanField("Remember Me")
    submit = SubmitField("Login")

 # this is the registration form
class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    email = StringField("Email Address", validators=[Email("Please enter a valid email")])
    #linking two fields - password should be equal to data entered in confirm
    password=PasswordField("Password", validators=[InputRequired()])
    confirm = PasswordField("Confirm Password", validators=[InputRequired(), EqualTo('password')])
    address = StringField("Address")
    contactNumber = StringField("Phone Number", validators=[InputRequired(),])

    #submit button
    submit = SubmitField("Register")

    # Check to ensure username is not already taken
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("Username Taken")
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("Email Taken")

# Create event form
class CreateEventForm(FlaskForm):
    event_name=StringField("Event Name", validators=[InputRequired('Enter event name')])
    event_date=StringField("Event date", validators=[InputRequired('Enter date of event')])
    event_time=StringField("Start at:", validators=[InputRequired('Enter time of event')])
    event_description=StringField("Description of event", validators=[InputRequired('Enter a desciption of the event')])
    ticket_price = StringField('Ticket price', validators=[InputRequired()])
    event_status = SelectField("Event Status", choices=(("open", "Open"), ("closed","Closed"), ("sold out", "Sold Out"), ("cancelled", "Cancelled"), ("unpublished", "Unpublished")))
    # event_img=FileField('Destination Image', validators=[FileRequired(message='Image cannot be empty'),FileAllowed(ALLOWED_FILE, message='Only supports png,jpg,JPG,PNG')])
    submit = SubmitField("Create Event")

# Used to find event info for event of user's choice
class FindEventForm(FlaskForm):
    event_id = SelectField('Event', choices=[])
    submit = SubmitField("Find Event Details")

