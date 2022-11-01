#!/usr/bin/python3
"""Review Class module for the project"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class for storing reviews"""
    place_id = ""
    user_id = ""
    text = ""
