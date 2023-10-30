#!/usr/bin/python3
""" This module implement a rule that returns the status of the application"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ returns a Json """
    return jsonify({"status": "OK"})

@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def get_stats():
    """Retrieves the number of each object type."""
    classes = {
        "amenity": storage.count(Amenity),
        "city": storage.count(City),
        "place": storage.count(Place),
        "review": storage.count(Review),
        "state": storage.count(State),
        "user": storage.count(User)
    }
    return jsonify(classes)


if __name__ == "__main__":
    pass
