#!/usr/bin/python3
"""City Class Module for the project"""
from models.base_model import BaseModel


class City(BaseModel):
    """ The city class, contains state ID and name"""
    state_id = ""
    name = ""
