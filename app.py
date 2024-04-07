# imports
import json
from flask import Flask
from src.controllers.controller_main import weather_stats
from flask_cors import CORS
from mongoengine import connect

import os

config_path = os.environ.get("CONFIG_PATH", "config.json")

with open(config_path, 'r') as f:
    config = json.load(f)

app = Flask(config["APP_NAME"])
app.config.update(config)

CORS(app)

# set a 'SECRET_KEY' to enable the Flask session cookies
app.config["TESTING"] = config["TESTING"]
app.config['SECRET_KEY'] = config["SECRET_KEY"]


DB_URI = config["DB_PICOLTE"]["DB_URI"]

connect(host=DB_URI)

# ----------------------------------------------------
# * Login Register routes start

app.add_url_rule("/weather-stats", view_func=weather_stats,
                 methods=["GET", "POST"])





