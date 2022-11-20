from flask import Flask
from view import home, sign_in, sign_up, about, menu, contact_us
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dfe9442eb154ab74e01e7e7d063fcdf8'

app.add_url_rule('/', 'home', home.home)
app.add_url_rule('/sign up', 'sign_up', sign_up.sign_up, methods=['GET','POST'])
app.add_url_rule('/sign in', 'sign_in', sign_in.sign_in, methods=['GET','POST'])
app.add_url_rule('/about', 'about', about.about)
app.add_url_rule('/menu', 'menu', menu.menu)
app.add_url_rule('/contact us', 'contact_us', contact_us.contact_us)




