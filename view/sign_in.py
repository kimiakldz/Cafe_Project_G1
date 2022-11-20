from flask import render_template
from view.form import SignInForm


def sign_in():
    form = SignInForm()
    return render_template('sign_in.html', form=form, title='Sign In')
