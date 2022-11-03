
from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField,SubmitField, StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email, EqualTo
from flask_wtf.file import FileRequired, FileField, FileAllowed

ALLOWED_FILE = {'PNG','JPG','png','jpg'}

#creates the login information
class LoginForm(FlaskForm):
    username=StringField("Username", validators=[InputRequired('Enter username')])
    password=PasswordField("Password", validators=[InputRequired('Enter password')])
    submit = SubmitField("Login")

 # this is the registration form
class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    email = StringField("Email Address", validators=[Email("Please enter a valid email")])
    #linking two fields - password should be equal to data entered in confirm
    password=PasswordField("Password", validators=[InputRequired()])
    confirm = PasswordField("Confirm Password", validators=[InputRequired(), EqualTo('password')])
    address = StringField("Address")
    contact_number = StringField("Phone Number", validators=[InputRequired(),])

    #submit button
    submit = SubmitField("Register")

# Create event form
class CreateEventForm(FlaskForm):
    event_name=StringField("Event Name", validators=[InputRequired('Enter event name')])
    event_date=StringField("Event date", validators=[InputRequired('Enter date of event')])
    event_description=StringField("Description of event", validators=[InputRequired('Enter a desciption of the event')])
    ticket_price = StringField('Ticket price', validators=[InputRequired()])
    event_img=FileField('Destination Image', validators=[FileRequired(message='Image cannot be empty'),FileAllowed(ALLOWED_FILE, message='Only supports png,jpg,JPG,PNG')])
    submit = SubmitField("Create Event")