#!/usr/bin/python3
"""User class module for the project"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class handles the record information of users"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
