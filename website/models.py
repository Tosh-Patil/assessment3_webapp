from . import db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func  # Used for datetime object
from flask_login import UserMixin


# Defines the parameters for the 'User' db table
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    name = db.Column(db.String(64))
    address = db.Column(db.String(128))
    contactNumber = db.Column(db.String(32))
    comments = db.relationship('Comment', backref='user', lazy=True)
    events = db.relationship('Event', backref='user', lazy=True)
    ticketorders = db.relationship('ticketOrder', backref='user', lazy=True)


# Defines the parameters for the 'Events' db table
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    eventName = db.Column(db.string(64), nullable=False)
    eventDate = db.Column(db.String(64), nullable=False)
    ticketTypes = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(2048), nullable=False)
    eventStatus = db.Column(db.String(32), nullable=False)
    comments = db.relationship('Comment', backref='event', lazy=True)
    ticketOrders = db.relationship('ticketOrder', backref='event', lazy=True)


# Defines the parameters for the 'Comments' db table
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    eventId = db.Column(db.Integer, db.ForeignKey('event.id'),
        nullable=False)
    content = db.Column(db.String(512), nullable=False)
    timeCommented = db.Column(db.DateTime(timezone=True),
        server_default=func.now())


# Defines the parameters for the 'ticketOrders' db table
class ticketOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    eventId = db.Column(db.Integer, db.ForeignKey('event.id'),
        nullable=False)
    ticketType = db.Column(db.String(32), nullable=False)
