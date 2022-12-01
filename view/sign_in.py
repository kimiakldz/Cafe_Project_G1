from core.manager import bcrypt
from flask import render_template, url_for, flash, redirect, request
from view.form import SignInForm
from models.user import User
from flask_login import login_user, current_user
# from flask_security import login_user


def sign_in():
    form = SignInForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash(f'{current_user.f_name}, successful login', 'success')
            return redirect(f'{next_page}' if next_page else url_for('home'))
        else:
            flash('Your email or your password is wrong!', 'danger')
    return render_template('sign_in.html', form=form, title='Sign In')

