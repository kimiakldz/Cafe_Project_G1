from flask import request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin, AdminIndexView
from flask_security import Security, SQLAlchemyUserDatastore
from app import app


# create the extension
db = SQLAlchemy()
# create bcrypt to hash password
bcrypt = Bcrypt(app)
# configure the SQLite database, relative to the app instance folder
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
username = 'myuser'
password = '17041369'
database = 'cafe_project'
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{username}:{password}@localhost:5432/{database}"
# initialize the app with the extension
db.init_app(app)
# create login manager
login_manager = LoginManager(app)

app.config["SECURITY_PASSWORD_SALT"] = "203882647964731086208225376307892472841"


class MyModelView(ModelView):
    def is_accessible(self):
        # return True
        return current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('sign_in', next=request.url))


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        # return True
        return current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('sign_in', next=request.url))


# Setup Flask-Security
from models.user import User, Role
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app=app, datastore=user_datastore)

# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'superhero'
admin = Admin(app, name='Cafe', template_mode='bootstrap3', index_view=MyAdminIndexView())
from view.cashier import *


