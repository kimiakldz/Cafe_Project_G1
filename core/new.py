from app import app
from core.manager import db, user_datastore, bcrypt
from core.manager import bcrypt
from models.menuitem import Menu
from models.user import User, Role
from models.table import Table
from models.reciept import Receipt
from models.orders import Order, Status


with app.app_context():
    db.create_all()
with app.app_context():
    # creating an admin
    admin = user_datastore.create_role(name="admin")
    hash_password = bcrypt.generate_password_hash('admin2022').decode('utf-8')
    user = user_datastore.create_user(f_name='admin', l_name='admin', email='admin@cafeproject.com', password=hash_password)
    user_datastore.add_role_to_user(user, 'admin')
    # creating a user
    user = user_datastore.create_role(name="user")
    hash_password = bcrypt.generate_password_hash('user2022').decode('utf-8')
    user = user_datastore.create_user(f_name='user', l_name='user', email='user@cafeproject.com', password=hash_password )
    user_datastore.add_role_to_user(user, 'user')

    # creating cafe's tables
    for i in range(1,5):
        table = Table(table_number=i, position=f"pos{i}")
        db.session.add(table)

    # creating menu item
    for i in range(1, 5):
        item = Menu(name=f"item{i}", category=f"cat{i}", price=i*1000, discount=0, image='static/images/Cappuccino.jpg')
        db.session.add(item)

    # Order Status:
    ordered = Status(name='ordered')
    cooking = Status(name='cooking')
    delivered = Status(name='delivered')
    db.session.add(ordered)
    db.session.add(cooking)
    db.session.add(delivered)
    # add to database
    db.session.commit()



