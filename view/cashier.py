from flask import render_template


def cashier():
    return render_template('cashier.html', title='About')
