#!/usr/bin/python3
""" init py file """
from flask import Blueprint


app_views = Blueprint("app_views", __name__, url_prefix='/api/v1')

from api.v1.views import index, states, cities, amenities, users
from api.v1.views import places, places_reviews, place_amenities
