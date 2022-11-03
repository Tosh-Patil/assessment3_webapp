from flask import ( 
    Blueprint, flash, render_template, request, url_for, redirect
) 
from werkzeug.security import generate_password_hash,check_password_hash
from .models import User
from .forms import LoginForm,RegisterForm
from flask_login import login_user, login_required,logout_user
from . import db


#create a blueprint
bp = Blueprint('auth', __name__, template_folder='templates')


# registration function
@bp.route('/register', methods =['GET', 'POST'])
def register():
    #create the form
    form = RegisterForm()
    if form.validate_on_submit():
        print('Register form submitted')

        uname = form.user_name.data
        pwd = form.password.data
        email = form.email_id.data
        name = form.name.data
        address = form.address.data
        contact = form.contact_number.data

        pwd_hash = generate_password_hash(pwd)

        new_user = User(username=uname, email=email, password=pwd, name=name, address=address, contactNumber=contact)
        db.session.add(new_user)
        db.session.commit
        flash('Registered Account')
        return redirect(url_for('auth.register'))

    return render_template('user.html', form=form, heading='REGISTER')



# login function
@bp.route('/login', methods=['GET', 'POST'])
def authenticate(): #view function
    print('In Login View function')
    login_form = LoginForm()
    error=None
    if(login_form.validate_on_submit()==True):
        user_name = login_form.user_name.data
        password = login_form.password.data
        u1 = User.query.filter_by(name=user_name).first()
        if u1 is None:
            error='Incorrect user name'
        elif not check_password_hash(u1.password_hash, password): # takes the hash and password
            error='Incorrect password'
        if error is None:
            login_user(u1)
            nextp = request.args.get('next') #this gives the url from where the login page was accessed
            print(nextp)
            if next is None or not nextp.startswith('/'):
                return redirect(url_for('index'))
            return redirect(nextp)
        else:
            flash(error)
    return render_template('user.html', form=login_form, heading='Login')


@bp.route('/logout')
def logout():
    logout_user()
    return redirect('/index')
