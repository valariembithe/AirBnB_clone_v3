#!/usr/bin/python3
"""
    Handles all default RESTFul API actions between Places and Amenities
"""
from flask import Flask, jsonify, request, abort
from models import storage
from api.v1.views import app_views
from models.place import Place
from models.amenity import Amenity
from models import storage_t as storage_type

@app_views.route('/places/<place_id>/amenities', methods=['GET'], strict_slashes=False)
def get_amenities(place_id):
    """ Retrieves the list of all Amenity objects of a Place """
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    if storage_type == 'db':
        amenities = [amenity.to_dict() for amenity in place.amenities]
    return jsonify(amenities)

@app_views.route('/amenities/<amenity_id>', methods=['GET'], strict_slashes=False)
def get_amenity(amenity_id):
    """ Retrieve one Amenity """
    amentity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    return jsonify(amenity.to_dict)
    

@app_views.route('/places/<place_id>/amenities/<amenity_id>', 
        methods=['DELETE'], strict_slashes=False)
def delete_amenity(place_id, amenity_id):
    """ Deletes a Amenity object to a Place """
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    if amenity not in place.amenities:
        abort(404)
    if storage_type == 'db':
        place.amenities.remove(amenity)
    else:
        place.amenity_ids.remove(amenity)
    storage.save()
    return jsonify({}), 200

@app_views.route('/places/<place_id>/amenities/<amenity_id>', 
        methods=['POST'], strict_slashes=False)
def create_amenity(place_id, amenity_id):
    """ Link a Amenity object to a Place: POST """
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    if amenity in place.amenities:
        return jsonify({amenity.to_dict()}), 200
    if storage_type == 'db':
        place.amenities.append(amenity)
    else:
        place.amenity_ids.append(amenity)
    storage.save()
    return jsonify({amenity.to_dict()}), 201
