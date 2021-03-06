import logging
import os
from logging.handlers import RotatingFileHandler

from flask import Flask


def config_logger(app: Flask):
    path = os.path.join(app.instance_path, 'log')
    if not os.path.isdir(path):
        os.mkdir(path)
    formatter = logging.Formatter("[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
    handler = RotatingFileHandler(os.path.join(app.instance_path, 'log', 'app.log'), maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
