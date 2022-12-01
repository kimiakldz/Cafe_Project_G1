from core.manager import db


class Table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    table_number = db.Column(db.Integer, nullable=False)
    position = db.Column(db.String, nullable=False)


