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


class Table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    table_number = db.Column(db.Integer, nullable=False)
    position = db.Column(db.String, nullable=False)


