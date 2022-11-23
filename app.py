from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dfe9442eb154ab74e01e7e7d063fcdf8'

from view.home import home
from view.sign_in import sign_in
from view.sign_up import sign_up
from view.sign_out import sign_out
from view.menu import menu
from view.contact_us import contact_us


app.add_url_rule('/', 'home', home)
app.add_url_rule('/sign up', 'sign_up', sign_up, methods=['GET', 'POST'])
app.add_url_rule('/sign in', 'sign_in', sign_in, methods=['GET', 'POST'])
app.add_url_rule('/sign out', 'sign_out', sign_out)
app.add_url_rule('/menu', 'menu', menu)
app.add_url_rule('/contact us', 'contact_us', contact_us, methods=['GET', 'POST'])



