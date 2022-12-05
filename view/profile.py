# from app import app
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from view.form import UpdateProfile
from core.manager import db, bcrypt

from core.manager import login_manager

# @app.route('/sign in')
# @login_required
def profile():
    if current_user.is_authenticated:
        form = UpdateProfile()
        if request.method == 'GET':
            form.f_name.data = current_user.f_name
            form.l_name.data = current_user.l_name
            form.phone.data = current_user.phone
            form.address.data = current_user.address
            return render_template('profile.html', title="Profile", form=form)
        else:
            current_user.f_name = form.f_name.data
            current_user.l_name = form.l_name.data
            current_user.phone = form.phone.data
            current_user.address = form.address.data
            current_user.password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            db.session.commit()
            flash('your profile updated', 'info')
            return redirect(url_for('profile'))
    else:
        return redirect(url_for('sign_in'))