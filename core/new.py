from app import app
from core.manager import db
from models.menuitem import MenuItem
from models.user import User
from models.table import Table
from models.reciept import Receipt
from models.orders import Order


with app.app_context():
    db.create_all()

