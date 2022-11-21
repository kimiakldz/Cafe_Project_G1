from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from core.manager import db

# # create the extension
# db = SQLAlchemy()
# # create the app
# app = Flask(__name__)
# # configure the SQLite database, relative to the app instance folder
# app.config["SQLALCHEMY_DATABASE_URI"] = "postgres:///project.db"
# # initialize the app with the extension
# db.init_app(app)


class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    category = db.Column(db.String, unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    discount = db.Column(db.Float, nullable=False)
    cooking_time = db.Column(db.Integer)
    # serving_time_period =


