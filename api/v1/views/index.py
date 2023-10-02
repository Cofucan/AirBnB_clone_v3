#!/usr/bin/python3
""" The index file """
from flask import jsonify

from api.v1.views import app_views


@app_views.route("/status", methods=["GET"], strict_slashes=False)
def status():
    """Returns the status"""
    return jsonify(status="OK")
