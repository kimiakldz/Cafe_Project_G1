from flask import render_template, session, request


def cart():
    if request.method == "post":
        pass
    return render_template('cart.html')