from flask_sqlalchemy import SQLAlchemy
from app import app

# create the app

# create the extension
db = SQLAlchemy()
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres:///project.db"
# initialize the app with the extension
db.init_app(app)

# def create_app():
#     app = Flask(__name__)
#     db.init_app(app)
#     return app