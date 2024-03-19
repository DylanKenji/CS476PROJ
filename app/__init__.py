#initialize the app and the database
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#initialize the app and the database to use SQLAlchemy and Flask
app = Flask(__name__, instance_relative_config=True)
app.config["SECRET_KEY"] = "Gvu90ney4n5rv09w4"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///UR_CONNECT.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
UPLOAD_FOLDER = os.path.join(app.static_folder, 'library', 'media', 'Avatars')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = SQLAlchemy(app)

# import the views and models
from app import views
from app import models

