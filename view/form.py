from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, validators, TextAreaField


class SignUpForm(FlaskForm):
    f_name = StringField('First Name', [validators.DataRequired()])
    l_name = StringField('Last Name', [validators.DataRequired()])
    phone = StringField('Phone')
    email = StringField('Email', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])
    confirm_password = PasswordField('Confirm Password', [validators.DataRequired(), validators.EqualTo(password)])
    address = StringField('Address')
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
    message = TextAreaField('Message', [validators.DataRequired()])
    copy = BooleanField('Send copy to my email')
    submit = SubmitField('Send')
