from flask import render_template, redirect, url_for, session, request
from models.orders import Order
from flask_login import login_required, current_user
from core.manager import db


def merge_dicts(dict1, dict2):
    # if isinstance(dict1, list) and isinstance(dict2, list):
    #     return dict1+dict2
    # elif isinstance(dict1, dict) and isinstance(dict2, dict):
    return dict(list(dict1.items())+list(dict2.items())) # [1,{'name': tea, 'price': 20000}],[2,{'name': coffee, 'price': 25000}]
    # return False


def order():
    item_id = request.form.get('item_id')     #1   #2
    item_name = request.form.get('item_name')  # tea #coffee
    item_price = request.form.get('item_price') # 20000 #25000
    if item_id and request.method == 'POST':
        dict_items = {item_id: {'name': item_name, 'price': item_price}}
        # {1:{'name': 'tea', 'price': 20000}}
        # {2:{'name': 'coffee', 'price': 25000}}
        if 'orders' in session:
            session['orders'] = merge_dicts(session['orders'], dict_items)
        else:
            session['orders'] = dict_items # session['orders']= {1:{'name': 'tea', 'price': 20000}}
            return redirect(request.referrer)
    return redirect(request.referrer)











