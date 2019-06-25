import os
import sys

import connexion
from flask_pymongo import PyMongo
from flask_marshmallow import Marshmallow

from api_settings.mongo import mongo_uri


drive_letter = os.path.splitdrive(sys.executable)[0]
if drive_letter:
    drive_letter += '\\'
else:
    drive_letter = r'/'
text_files_dir = os.path.join(drive_letter, 'data', 'text_files')

basedir = os.path.abspath(os.path.dirname(__file__))
connex_app = connexion.App(__name__, specification_dir=basedir)
connex_app.add_api("rest_api.yml")

flask_app = connex_app.app

flask_app.config["MONGO_URI"] = mongo_uri

mongo = PyMongo(flask_app)
ma = Marshmallow(flask_app)

