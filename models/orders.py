from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from core.manager import db
from datetime import datetime
from sqlalchemy.types import Boolean, Date, DateTime, Float, Integer, Text, Time, Interval
from models.menuitem import Menu
from models.reciept import Receipt


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    menu_id = db.Column(db.Integer, db.ForeignKey('menu.id'), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    receipt_id = db.Column(db.Integer, db.ForeignKey(Receipt.id), nullable=False)
    order_status = db.Column(db.Integer, db.ForeignKey('status.id'), nullable=False)
    time_stamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


class Status(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)



