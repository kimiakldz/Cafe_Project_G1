from flask import render_template, redirect, url_for, flash
from view.form import SignUpForm


def sign_up():
    form = SignUpForm()
    # if form.validate_on_submit():
    #     flash(f"Account created for {form.username.data}!", "success")
    #     return redirect({{url_for('home')}})
    return render_template('sign_up.html', form=form,  title='Sign Up')
