from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from core.manager import db
from table import Table
from user import User
# # create the extension
# db = SQLAlchemy()
# # create the app
# app = Flask(__name__)
# # configure the SQLite database, relative to the app instance folder
# app.config["SQLALCHEMY_DATABASE_URI"] = "postgres:///project.db"
# # initialize the app with the extension
# db.init_app(app)


class Receipt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    table_id = db.Column(db.Integer, db.ForeigKey('Table.id'), nullable=False)
    user_id = db.Column(db.Integer,db.ForeigKey('User.id'), nullable=False)

