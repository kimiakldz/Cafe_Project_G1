from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from core.manager import db


class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    category = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    discount = db.Column(db.Float, nullable=False)
    cooking_time = db.Column(db.Integer)
    image = db.Column(db.String)
    # serving_time_period =

