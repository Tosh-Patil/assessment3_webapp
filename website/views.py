from flask import Blueprint
from flask import Flask
from flask import render_template

bp = Blueprint('main', __name__, template_folder='templates')


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/user', methods=['GET', 'POST'])
def user():
    return render_template('user.html')
