import os
import sys
import yaml

import connexion
from flask_pymongo import PyMongo
from flask_marshmallow import Marshmallow


basedir = os.path.abspath(os.path.dirname(__file__))
connex_app = connexion.App(__name__, specification_dir=basedir)

flask_app = connex_app.app

# TODO leave this hardcoded for now
env = 'dev'

settings_file = os.path.join(basedir, 'settings.yml')

yml = {}
with open(settings_file) as f:
    yml = yaml.safe_load(f)[env]

port = yml['port']

drive_letter = os.path.splitdrive(sys.executable)[0]
if drive_letter:
    drive_letter += '\\'
else:
    drive_letter = r'/'
text_files_dir = os.path.join(drive_letter, 'data', 'text_files')

connex_app.add_api("rest_api.yml")

flask_app.config["MONGO_URI"] = yml['mongo_uri']

mongo = PyMongo(flask_app)
ma = Marshmallow(flask_app)
