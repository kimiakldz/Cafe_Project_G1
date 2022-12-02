from flask import render_template, redirect, url_for, flash, request
from flask_security.utils import hash_password
from view.form import SignUpForm
from models.user import User
from core.manager import bcrypt, db, user_datastore


def sign_up():
    form = SignUpForm()
    # if form.validate_on_submit():
    if request.method == 'POST':
        # user = user_datastore.create_user(f_name=form.f_name.data, l_name=form.l_name.data, email=form.email.data,
        #                                   phone=form.phone.data, password=hash_password(form.password.data))
        user = User(f_name=form.f_name.data, l_name=form.l_name.data, email=form.email.data,
        phone=form.phone.data, password=bcrypt.generate_password_hash(form.password.data).decode('utf-8'))
        db.session.add(user)
        db.session.commit()
        flash(f"Account created for {form.f_name.data} {form.l_name.data}!", "success")
        return redirect(url_for('home'))
    return render_template('sign_up.html', form=form,  title='Sign Up')


