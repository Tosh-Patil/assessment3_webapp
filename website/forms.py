
from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField,SubmitField, StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email, EqualTo


#creates the login information
class LoginForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired('Enter user name')])
    password=PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

 # this is the registration form
class RegisterForm(FlaskForm):
    user_name = StringField("User Name", validators=[InputRequired()])
    email_id = StringField("Email Address", validators=[Email("Please enter a valid email")])
    #linking two fields - password should be equal to data entered in confirm
    password=PasswordField("Password", validators=[InputRequired(),
                  EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")
    name = StringField("Name", validators=[InputRequired()])
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
    event_img=FileField('Destination Image', validators=[
    FileRequired(message='Image cannot be empty'),
    FileAllowed(ALLOWED_FILE, message='Only supports png,jpg,JPG,PNG')])
    submit = SubmitField("Create Event")