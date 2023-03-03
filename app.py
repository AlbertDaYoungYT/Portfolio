from __future__ import division
import data.settings as S
import os
os.system(".\\build.bat")

from loguru import logger

logger.add(
    "./logs/{time}.log", rotation=S.LOG_ROTATION_SIZE, retention=S.LOG_RETENTION_TIME
)


import base64
from flask import *
from werkzeug.utils import *
from flask_cors import CORS
from datetime import datetime, timedelta, date
import hashlib
import random
import stripe
import uuid
import re
logger.success("Imported External Modules")

import modules.core as core
import modules.core.auth as auth
import modules.core.cache as cache
import modules.core.document as document
import db as DB
logger.success("Imported Internal Modules")


UPLOAD_FOLDER = "static/favicons/uploads"
EMAIL_REGEX = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

app = Flask(__name__)
CORS(app)
app.secret_key = S.SECRET
stripe.api_key = S.STRIPE
app.config["SESSION_TYPE"] = "filesystem"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024
logger.success("Initiated Flask")

import click
def secho(text, file=None, nl=None, err=None, color=None, **styles):
    pass

def echo(text, file=None, nl=None, err=None, color=None, **styles):
    pass

click.echo = echo
click.secho = secho

import logging
log = logging.getLogger('werkzeug')
if S.DISABLE_FLASK_LOG:
    log.disabled = True
    logger.success(f"Disabled Flask Logging")
else:
    logger.success(f"Enabled Flask Logging")


def check_email(email):
    if re.fullmatch(EMAIL_REGEX, email):
        return True
    else:
        return False


def seconds_to_hhmmss(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%d:%02d:%02d" % (hour, minutes, seconds)



@app.route("/")
def HomePage():
    return render_template("index.html", SiteName="Home")



try:
    if os.name == 'nt':
        app.run(host="0.0.0.0", port=443, debug=True, ssl_context=("cert.pem", "key.pem"))
    else:
        app.run(host="0.0.0.0", port=5000, debug=True)
except Exception as e:
    os.system("openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365")
finally:
    if os.name == 'nt':
        app.run(host="0.0.0.0", port=443, debug=True, ssl_context=("cert.pem", "key.pem"))
    else:
        app.run(host="0.0.0.0", port=5000, debug=True)
