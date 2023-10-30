#!/usr/bin/python3
""" This module implement a rule that returns the status of the application"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ returns a Json """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def get_stats():
    """Retrieves the number of each object type."""
    classes = {
        "Amenity": storage.count(Amenity),
        "City": storage.count(City),
        "Place": storage.count(Place),
        "Review": storage.count(Review),
        "State": storage.count(State),
        "User": storage.count(User)
    }
    return jsonify(classes)
