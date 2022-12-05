from core.manager import admin, db, MyModelView
from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView
from flask_security import current_user
from models.user import User, Role
from models.orders import Order
from models.table import Table
from models.menuitem import Menu
from models.reciept import Receipt


admin.add_view(MyModelView(User, db.session))
admin.add_view(MyModelView(Order, db.session))
admin.add_view(MyModelView(Table, db.session))
admin.add_view(MyModelView(Menu, db.session))
admin.add_view(MyModelView(Receipt, db.session))
admin.add_view(MyModelView(Role, db.session))

# def cashier():
#     return render_template('cashier.html', title='Cashier')
#
#
# def menu_management():
#     # add_new_item
#     # delete_item
#     # update_item
#     # show_items
#     pass
#
# def order_management():
#     # order_status
#     # cancel_order
#
# def comment_management():
#     pass


