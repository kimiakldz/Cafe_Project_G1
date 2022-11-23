from flask import url_for,flash,redirect
from flask_login import logout_user


def sign_out():
    logout_user()
    flash('successful login','success')
    return redirect(url_for('home'))