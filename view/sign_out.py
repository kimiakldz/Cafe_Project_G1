from flask import url_for, flash, redirect
from flask_login import logout_user, current_user


def sign_out():
    name = current_user.f_name
    logout_user()
    flash(f'{name}, successful logout', 'success')
    return redirect(url_for('home'))
