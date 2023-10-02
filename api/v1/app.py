#!/usr/bin/python3
"""This module starts a simple flask app
"""
import os
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)
API_HOST = os.getenv(
        "HBNB_API_HOST",
        '0.0.0.0')
API_PORT = int(
        os.getenv("HBNB_API_PORT", "5000"))


@app.teardown_appcontext
def teardown_app(exception):
    """Close SQLAlchemy session or reload file storage session """
    storage.close()

@app.errorhandler(404)
def error_404(err):
    '''Handles the 404 HTTP error code.'''
    return jsonify(error='Not found'), 404


if __name__ == "__main__":
    app.run(
            host=API_HOST,
            port=API_PORT,
            threaded=True)
