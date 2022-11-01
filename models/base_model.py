#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """The BaseModel for the HBnB Project classes."""

    def __init__(self, *args, **kwargs):
        """Instantiate a new Basemodel.

        Args:
        *args (any): Unused.
        **kwargs (dict): Key/value pairs of attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            model.storage.new(self)

    def __str__(self):
        """Returns the print/sting of the BaseModel instance."""

        clname = self.__class___.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)

    def save(self):
        """Updates the updated_at instance with the current datetime."""

        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Returns the dictionary of the BaseModel instances."""

        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict
