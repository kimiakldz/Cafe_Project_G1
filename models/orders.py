from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from core.manager import db
from datetime import datetime
from sqlalchemy.types import Boolean, Date, DateTime, Float, Integer, Text, Time, Interval
from menuitem import MenuItem
from reciept import Receipt

# # create the extension
# db = SQLAlchemy()
# # create the app
# app = Flask(__name__)
# # configure the SQLite database, relative to the app instance folder
# app.config["SQLALCHEMY_DATABASE_URI"] = "postgres:///project.db"
# # initialize the app with the extension
# db.init_app(app)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    menu_id = db.Column(db.Integer, db.ForeignKey('MenuItem.id'), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    receipt_id = db.Column(db.Integer, db.ForeignKey('Receipt.id'), nullable=False)
    order_status = db.Column(db.String, nullable=False)
    time_stamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

