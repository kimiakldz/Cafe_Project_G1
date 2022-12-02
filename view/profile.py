# from app import app
from flask import render_template
from flask_login import login_required, current_user

from core.manager import login_manager

# @app.route('/sign in')
@login_required
def profile():
    return render_template('profile.html', title="Profile")
