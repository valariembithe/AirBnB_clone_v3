#!/usr/bin/python3
"""
    Handles all default RESTFul API actions between Places and Amenities
"""
from flask import Flask, jsonify, request, abort
from models import storage
from api.v1.views import app_views
from models.place import Place
from models.amenity import Amenity

@app_views.route('/places/<place_id>/amenities', 
        methods=['GET'], strict_slashes=False)
def get_amenities(place_id):
    """ Retrieves the list of all Amenity objects of a Place """
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    amenities = [amenity.to_dict() for amenity in place.amenities]
    return jsonify(amenities)

@app_views.route('/amenities/<amenity_id>', methods=['GET'], strict_slashes=False)
def get_amenity(amenity_id):
    """ Retrieve one Amenity """
    amentity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    return jsonify(amenity.to_dict)
    

@app_views.route('/amenities/<amenity_id>', methods=['DELETE'], strict_slashes=False)
def delete_amenity(amenity_id):
    """ Deletes a Amenity object to a Place """
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    if amenity not in place.amenities:
        abort(404)
    storage.delete(amenity)
    storage.save()
    return jsonify({}), 200

@app_views.route('/places/<place_id>/amenities', methods=['POST'], strict_slashes=False)
def create_amenity(place_id):
    """ Link a Amenity object to a Place: POST """
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    if amenity in place.amenities:
        return jsonify({amenity.to_dict()}), 200
    place.amenities.append(amenity)
    storage.save()
    return jsonify({amenity.to_dict()}), 201
