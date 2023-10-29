#!/usr/bin/python3
""" This module implement a rule that returns the status of the application"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ returns a Json """
    return jsonify({"status": "OK"})
