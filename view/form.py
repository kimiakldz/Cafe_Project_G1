from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, validators


class SignUpForm(FlaskForm):
    username = StringField('Username', [validators.DataRequired()])
    email = StringField('Email', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])
    confirm_password = PasswordField('Confirm Password', [validators.DataRequired(), validators.equal_to(password)])
    submit = SubmitField('Sign Up')


class SignInForm(FlaskForm):
    email = StringField('Email', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class ContactForm(FlaskForm):
    name = StringField('Name', [validators.DataRequired()])
    email = StringField('Email', [validators.DataRequired()])
    phone = PasswordField('Phone', [validators.DataRequired()])
    message = StringField('Message', [validators.DataRequired()])
    copy = BooleanField('Send copy to my email')
    submit = SubmitField('Send')
