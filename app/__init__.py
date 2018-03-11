#
# To execute the app, go to the command line and top level directory:
#
# set FLASK_APP=microblog.py   (or export for UNIX)
# flask run
#
#
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes
