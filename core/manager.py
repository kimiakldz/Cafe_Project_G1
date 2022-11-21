from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from app import app


# create the extension
db = SQLAlchemy()
# create bcrypt to hash password
bcrypt=Bcrypt(app)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)
# create login manager
login_manager=LoginManager(app)


