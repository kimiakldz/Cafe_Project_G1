from flask import render_template


def cashier():
    return render_template('cashier.html', title='Cashier')


def menu_management():
    # add_new_item
    # delete_item
    # update_item
    # show_items
    pass

def order_management():
    # order_status
    # cancel_order

def comment_management():
    pass


