from core.manager import bcrypt
from flask import render_template,url_for,flash,redirect
from view.form import SignInForm
from models.user import User
from flask_login import login_user


def sign_in():
    form = SignInForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            flash('successful login','success')
            return redirect(url_for('home'))
    return render_template('sign_in.html', form=form, title='Sign In')

