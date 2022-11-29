from core.manager import admin1, session
from flask_admin.contrib.sqla import ModelView
from models.user import User
from models.orders import Order
from models.table import Table
from models.menuitem import MenuItem
from models.reciept import Reciept

admin1.add_view(ModelView(User, session))
admin1.add_view(ModelView(Order, session))
admin1.add_view(ModelView(Table, session))
admin1.add_view(ModelView(MenuItem, session))
admin1.add_view(ModelView(Reciept, session))

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


