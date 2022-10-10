from . import db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func  # Used for datetime object


# Defines the parameters for the 'User' db table
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    name = db.Column(db.String(64))
    address = db.Column(db.String(128))
    contactNumber = db.Column(db.String(32))


# Defines the parameters for the 'Events' db table
class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'),
        nullable=False)
    eventDate = db.Column(db.String(64), nullable=False)
    ticketTypes = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(2048), nullable=False)
    eventStatus = db.Column(db.String(32), nullable=False)


# Defines the parameters for the 'Comments' db table
class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'),
        nullable=False)
    eventId = db.Column(db.Integer, db.ForeignKey('events.id'),
        nullable=False)
    content = db.Column(db.String(512), nullable=False)
    timeCommented = db.Column(db.DateTime(timezone=True),
        server_default=func.now())


# Defines the parameters for the 'ticketOrders' db table
class ticketOrders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'),
        nullable=False)
    eventId = db.Column(db.Integer, db.ForeignKey('events.id'),
        nullable=False)
    ticketType = db.Column(db.String(32), nullable=False)
