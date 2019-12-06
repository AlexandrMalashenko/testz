import logging
from logging.handlers import RotatingFileHandler


from flask import Flask

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

handler = RotatingFileHandler('logs.log', maxBytes=10000, backupCount=1)
app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)

from app import routes
