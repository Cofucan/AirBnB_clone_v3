#!/usr/bin/python3
""" """
from os import getenv

from flask import Flask

from api.v1.views import app_views
from models import storage

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == "__main__":
    env_host = getenv("HBNB_API_HOST", "0.0.0.0")
    env_port = getenv("HBNB_API_PORT", 5000)
    app.run(host=env_host, port=env_port, threaded=True)
