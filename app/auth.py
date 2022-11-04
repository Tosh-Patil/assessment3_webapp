from flask import ( 
    Blueprint, flash, render_template, request, url_for, redirect, session
) 
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from .forms import LoginForm,RegisterForm
from flask_login import login_user, login_required, logout_user, current_user 
from . import db


#create a blueprint
bp = Blueprint('auth', __name__, template_folder='templates')


# registration function
@bp.route('/register', methods =['GET', 'POST'])
def register():
    #create the form
    form = RegisterForm()
    if form.validate_on_submit():
        pwd_hash = generate_password_hash(form.password.data)

        user = User(
            username=form.username.data,
            email=form.email.data,
            address=form.address.data,
            contactNumber=form.contactNumber.data,
            password=pwd_hash
        )

        db.session.add(user)
        db.session.commit()
        flash('Registered Account')
        return redirect('/index')

    return render_template('register.html', title='REGISTER', form=form)



# login function
@bp.route('/login', methods=['GET', 'POST'])
def authenticate(): #view function
    if current_user.is_authenticated:
        return redirect('/index')
    form = LoginForm()
    error=None
    if(form.validate_on_submit()==True):
        username = form.username.data
        password = form.password.data
        u1 = User.query.filter_by(username=form.username.data).first()
        if u1 is None:
            error='Incorrect user name'
        elif not check_password_hash(u1.password, password): # takes the hash and password
            error='Incorrect password'
        if error is None:
            login_user(u1, remember=form.rememberMe.data)
            session['UserID'] = u1.id
            return redirect('/index')
        else:
            flash(error)
    return render_template('login.html', form=form, heading='Login')


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/index')
