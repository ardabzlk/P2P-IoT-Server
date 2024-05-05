# imports
import json
from flask import Flask
from src.controllers.controller_main import weather_stats
from flask_cors import CORS
from mongoengine import connect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

import os

config_path = os.environ.get("CONFIG_PATH", "config.json")

with open(config_path, 'r') as f:
    config = json.load(f)

app = Flask(config["APP_NAME"])
app.config.update(config)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["500 per day", "60 per hour"],
    storage_uri="memory://",
)

CORS(app)

# set a 'SECRET_KEY' to enable the Flask session cookies
app.config["TESTING"] = config["TESTING"]
app.config['SECRET_KEY'] = config["SECRET_KEY"]


DB_URI = config["DB_PICOLTE"]["DB_URI"]

connect(host=DB_URI)

# ----------------------------------------------------
# * Login Register routes start

@app.route("/api/weather-stats", methods=["GET", "POST"])
@limiter.limit("1 per 10 second", override_defaults=False)
def handle_weather_stats():
    return weather_stats()




