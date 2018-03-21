#
# To execute the app, go to the command line and top level directory:
#
# set FLASK_APP=microblog.py   (or export for UNIX)
# flask run
#
#
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view='login'

from app import routes, models
