#!/usr/bin/python3
"""Place or location Class module for the project"""
from models.base_model import BaseModel


class Place(BaseModel):
    """This class handles the location or place information of the users"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
