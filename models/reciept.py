from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from core.manager import db
from models.table import Table
from models.user import User


class Receipt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    table_id = db.Column(db.Integer, db.ForeignKey(Table.id), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)

