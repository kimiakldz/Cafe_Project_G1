from app import app
from core.manager import db, user_datastore
from core.manager import bcrypt
from models.menuitem import MenuItem
from models.user import User, Role
from models.table import Table
from models.reciept import Receipt
from models.orders import Order

with app.app_context():
    db.create_all()

# admin_role = user_datastore.create_role(title="admin")
# admin = user_datastore.create_user(f_name='admin', l_name='admin', email='admin@cafeproject.com', password='admin1990')
# user_datastore.add_role_to_user(admin, 'admin')
# db.session.commit()

