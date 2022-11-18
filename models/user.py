from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from core.manager import db

# # create the extension
# db = SQLAlchemy()
# # create the app
# app = Flask(ـ_name__)
# # configure the SQLite database, relative to the app instance folder
# app.config["SQLALCHEMY_DATABASE_URI"] = "postgres:///project.db"
# # initialize the app with the extension
# db.init_app(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String, nullable=False)
    l_name = db.Column(db.String, nullable=False)
    phone = db.Column(db.String)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    address = db.Column(db.String)
